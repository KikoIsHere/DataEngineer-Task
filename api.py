from datetime import date

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import extract, func

from models import Base, Customer, Product, SalesReciepts
from conn import SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/customers/birthday")
def get_customers_with_birthday(db:Session = Depends(get_db)):
    customers = db.query(Customer).filter(Customer.birthdate == '1951-02-01').all()

    if customers is None:
        raise HTTPException(
            status_code=404,
            detail="No customer has birthday today"
        )

    return {'customers': customers}

@app.get("/products/top-selling-products/{year}")
def get_top_sellings_products(year:int, db:Session = Depends(get_db)):  
    reciepts = db.query(Product.product.label('product_name'), func.sum(SalesReciepts.quantity).label('total_sales')) \
    .filter(extract('year', SalesReciepts.transaction_date) == year, Product.id == SalesReciepts.product_id)

    reciepts = reciepts.group_by(SalesReciepts.product_id) \
    .order_by(func.sum(SalesReciepts.quantity).label('quantity').desc()).limit(10).all()

    if reciepts is None:
        raise HTTPException(
            status_code=404,
            detail="no reciepts found for this year"
        )

    return {'products': reciepts}

@app.get("/customers/last-order-per-customer")
def get_last_order_per_customer(db:Session = Depends(get_db)):
    customers = db.query(Customer.id    , Customer.customer_email, func.max(SalesReciepts.transaction_date).label('last_order_date')) \
    .filter(Customer.id == SalesReciepts.customer_id) \
    .group_by(SalesReciepts.customer_id).all()

    if customers is None:
        raise HTTPException(
            status_code=404,
            detail="This article does not exist"
        )

    return {"customers": customers}
