# job.py
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from sqlmodel import Session
from db.sqlite import engine
from model.product import Product


# Simple function to check the stock level for products under 10 quantity
def check_stock_level():
    with Session(engine) as session:
        low_stock_products = session.query(Product).filter(Product.stock < 10).all()
        if low_stock_products:
            for product in low_stock_products:
                logging.warning(f"Product {product.name} has low stock: {product.stock}")


# Start the scheduler
def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_stock_level, 'interval', seconds=60)
    scheduler.start()
