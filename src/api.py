from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from db.sqlite import engine
from model.product import Product, OrderRequest, StockUpdate

rest = APIRouter()


# Endpoint for create a product
@rest.post("/products")
def create_product(product: Product):
    with Session(engine) as session:
        db_product = Product(sku=product.sku, name=product.name)
        session.add(db_product)
        session.commit()
        session.refresh(db_product)
        return db_product


# Endpoint for update a product quantity
@rest.patch("/inventories/product/{product_id}")
def add_stock(stock_update: StockUpdate, product_id: int):
    with Session(engine) as session:
        product = session.exec(select(Product).where(Product.id == product_id)).first()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        product.stock += stock_update.stock
        session.commit()
    return {"message": "Stock updated"}


# Endpoint for create a product order
@rest.post("/orders")
def create_order(order: OrderRequest):
    with Session(engine) as session:
        product = session.exec(select(Product).where(Product.id == order.product_id)).first()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        if product.stock < order.quantity:
            raise HTTPException(status_code=400, detail="Not enough stock")
        product.stock -= order.quantity
        session.commit()
        session.refresh(product)
    return {"message": "Order completed"}
