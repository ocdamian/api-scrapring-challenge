
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: str
    promo_price: str

class RequestProducts(BaseModel):
    url: str

class ResponseModel(RequestProducts):
    products:list[Product]
