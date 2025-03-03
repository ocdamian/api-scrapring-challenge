from fastapi import FastAPI, APIRouter, HTTPException, status

from app.services.seleniumService import scrape_products

from app.models.productModel import Product, RequestProducts, ResponseModel

router = APIRouter(tags = ['Products'])

@router.post("/products",response_model=ResponseModel)
async def get_products(request: RequestProducts):
    products = scrape_products(request.url) 
    response = ResponseModel(
        url=request.url,
        products=products
    )
    return response