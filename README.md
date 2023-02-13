# DataEngineer-Task
Task for a Data Engineer Application

To use the application you need to first create a venv by typing "python -venv .env" ("pip install venv" if you don't have the library).
After creating a virtual environment you need to install the dependencies, you can do that by typing "python requirements.txt".

Now that everything is set and done you can start by running the "load_data.py" file to load all the data to the database that is gonna be used.
You can change the database that the data will be inserted in from the ".env" file by changing the value of the "MSSQL_CONN" variable to fit the SQL alchemy route.

After all the data is loaded to the database, you can start the Web Application by running the command "uvicorn api:app --port 8086  --reload", that will run an instance
of the api.py application.

Endpoints: 
- /customers/birthday
- /products/top-selling-products/{year}
- /customers/last-order-per-customer
