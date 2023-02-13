
sql_queries = {
    "customer" : """INSERT IGNORE INTO customer (id, home_store, customer_first_name, 
                        customer_email, customer_since, loyalty_card_number, birthdate, gender, birth_year) 
                        VALUES (%s, %s, %s, %s ,%s, %s, %s, %s, %s)""",


    "dates" : """INSERT IGNORE INTO dates (transaction_date, date_id, week_id, week_desc,
                    month_id, month_name, quarter_id, quarter_name, year_id) 
                    VALUES (%s, %s, %s, %s ,%s, %s, %s, %s, %s)""",


    "generations" : """INSERT IGNORE INTO generations (birth_year, generation)
                        VALUES (%s, %s)""",


    "pastry_inventory" : """INSERT IGNORE INTO pastry_inventory (sales_outlet_id, transaction_date, product_id,
                            start_of_day, quantity_sold, waste, waste_percentage) 
                            VALUES (%s, %s, %s, %s ,%s, %s, %s)""",


    "product" : """INSERT IGNORE INTO product (id, product_group, product_category, product_type, product, product_description,
                    unit_of_measure, current_wholesale_price, current_retail_price, tax_exempt, promo, new_product) 
                    VALUES (%s, %s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s)""",


    "sales_targets" : """INSERT IGNORE INTO sales_targets (`sales_outlet_id`, `year_month`, `beans_goal`, `beverage_goal`, `food_goal`, `merchandise_goal`, `total_goal`) VALUES (%s, %s, %s, %s ,%s, %s, %s)""",


    "sales_outlet" : """INSERT IGNORE INTO sales_outlet (id, sales_outlet_type, store_square_feet, store_adress,
                    store_city, store_state_province, store_telephone, store_postal_code, store_longitude, store_latitude, manager, neighbourhood) 
                    VALUES (%s, %s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s)""",


    "sales_reciepts" : """INSERT IGNORE INTO sales_reciepts (`transaction_id`, `transaction_date`, `transaction_time`, `sales_outlet_id`, `staff_id`,
                    `customer_id`, `instore`, `order`, `line_item_id`, `product_id`, `quantity`, `line_item_amount`, `unit_price`, `promo_item`) 
                    VALUES (%s, %s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",


    "staff" : """INSERT IGNORE INTO staff (id, first_name, last_name, position, start_date, location)
                VALUES (%s, %s, %s, %s, %s, %s)"""
}