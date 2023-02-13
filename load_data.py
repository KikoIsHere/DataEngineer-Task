import os 
import pandas as pd
import numpy as np
import logging

from conn import engine
from models import Base
from sql_queries import sql_queries


logging.basicConfig(level=logging.DEBUG)


dir_name = "data"
csv_files = ['staff.csv', 'product.csv', 'sales_outlet.csv', 'customer.csv', 'Dates.csv', 'generations.csv', 'pastry inventory.csv', 'sales targets.csv', 'sales_reciepts.csv']
Base.metadata.create_all(engine)


con = engine.raw_connection()

def extract_from_csv(file_to_process): 
    dataframe = pd.read_csv(file_to_process) 
    dataframe = dataframe.loc[:, ~dataframe.columns.str.contains('^Unnamed')]
    return dataframe

def insert_into_db(dataframe, query, file):
    cursor = con.cursor()
    my_data = []
    
    for row in dataframe.itertuples(index=False, name=None):
        my_data.append(row)
        logging.info(f'Extracting data from {file}: {row}')
    
    cursor.executemany(query, my_data)
    logging.info(f'Inserted data from {file} successfully')
    cursor.close()
    con.commit()

def format_date(dataframe, columns):
    for column in columns:
        try:
            dataframe[column] = pd.to_datetime(dataframe[column] , format='%m/%d/%Y')
        except KeyError:
            pass
    return dataframe

def format_boolean(dataframe):
    dataframe = dataframe.replace('Y', True)
    dataframe = dataframe.replace('N', False)
    return dataframe

def replace_nan(dataframe):
    dataframe = dataframe.replace(np.nan, None)
    return dataframe

for file in csv_files:
    query = sql_queries[file.replace('.csv', '').lower().replace(' ', '_')]

    df = extract_from_csv(os.path.join(dir_name, file))
    df = format_boolean(df)
    df = replace_nan(df)

    if file in ["staff.csv", "pastry inventory.csv", "Dates.csv"]:
        df = format_date(df, ['start_date', 'transaction_date'])
    

    insert_into_db(df, query, file)

con.close()