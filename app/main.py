
from fastapi import FastAPI, APIRouter

from .routers import  products

version = 'v1'
API_PREFIX = '/api/{version}'

app = FastAPI()
api_router = APIRouter(prefix=API_PREFIX)

api_router.include_router(products.router)

app.include_router(api_router)