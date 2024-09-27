# product.py
from pydantic import conint, BaseModel
from sqlmodel import SQLModel, Field


class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    sku: str
    name: str
    stock: int = Field(default=100)


class StockUpdate(BaseModel):
    stock: conint(gt=0)


class OrderRequest(BaseModel):
    product_id: conint(gt=0)
    quantity: conint(gt=0)
