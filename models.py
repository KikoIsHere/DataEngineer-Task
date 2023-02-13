from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, Float, Time
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    product_group = Column(String(256))
    product_type = Column(String(256))
    product_category = Column(String(256))
    product = Column(String(256))
    product_description = Column(String(256))
    unit_of_measure = Column(String(256))
    current_wholesale_price = Column(String(256))
    current_retail_price = Column(String(256))
    tax_exempt = Column(Boolean)
    promo = Column(Boolean)
    new_product = Column(Boolean)
    

class Dates(Base):
    __tablename__ = "dates"

    id = Column(Integer, primary_key=True)
    transaction_date = Column(Date)
    date_id = Column(Integer)
    week_id = Column(Integer)
    week_desc = Column(String(256))
    month_id = Column(Integer)
    month_name = Column(String(256))
    quarter_id = Column(Integer)
    quarter_name = Column(String(256))
    year_id = Column(Integer)

class Generations(Base):
    __tablename__ = "generations"

    id = Column(Integer, primary_key=True)
    birth_year = Column(Integer)
    generation = Column(String(256))


class PastryInventory(Base):
    __tablename__ = "pastry_inventory"

    id = Column(Integer, primary_key=True)
    sales_outlet_id = Column(ForeignKey("sales_outlet.id"))
    transaction_date = Column(Date)
    product_id = Column(ForeignKey("product.id"))
    start_of_day = Column(Integer)
    quantity_sold = Column(Integer)
    waste = Column(Integer)
    waste_percentage = Column(String(256))

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    home_store = Column(ForeignKey("sales_outlet.id"))
    customer_first_name = Column(String(256))
    customer_email = Column(String(256))
    customer_since = Column(Date)
    loyalty_card_number = Column(String(256))
    birthdate = Column(Date)
    Gender = Column(String(256))
    birth_year = Column(Integer)


class SalesTargets(Base):
    __tablename__ = "sales_targets"

    id = Column(Integer, primary_key=True)
    sales_outlet_id = Column(ForeignKey("sales_outlet.id"))
    year_month = Column(String(256))
    beans_goal = Column(Integer)
    beverage_goal = Column(Integer)
    food_goal = Column(Integer)
    merchandise_goal = Column(Integer)
    total_goal = Column(Integer)


class SalesOutlet(Base):
    __tablename__ = "sales_outlet"

    id = Column(Integer, primary_key=True)
    sales_outlet_type = Column(String(256))
    store_square_feet = Column(Integer)
    store_adress = Column(String(256))
    store_city = Column(String(256))
    store_state_province = Column(String(256))
    store_telephone = Column(String(256))
    store_postal_code = Column(Integer)
    store_longitude = Column(Float)
    store_latitude = Column(Float)
    manager = Column(ForeignKey("staff.id"), nullable=True)
    neighbourhood = Column(String(256))


class SalesReciepts(Base):
    __tablename__ = "sales_reciepts"

    id = Column(Integer, primary_key=True)
    transaction_id = Column(Integer)
    transaction_date = Column(Date)
    transaction_time = Column(Time)
    sales_outlet_id = Column(ForeignKey("sales_outlet.id"))
    staff_id = Column(ForeignKey("staff.id"))
    customer_id = Column(ForeignKey("customer.id"))
    instore = Column(Boolean)
    order = Column(Integer)
    line_item_id = Column(Integer)
    product_id = Column(ForeignKey("product.id"))
    quantity = Column(Integer)
    line_item_amount = Column(Float)
    unit_price = Column(Integer)
    promo_item = Column(Boolean)


class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(256))
    last_name = Column(String(256))
    position = Column(String(256))
    start_date = Column(Date)
    location = Column(String(256))


