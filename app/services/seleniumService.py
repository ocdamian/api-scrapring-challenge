from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from typing import List
from app.models.productModel import Product

def scrape_products(url: str) -> List[Product]:
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")  
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--remote-debugging-port=9222")  
    chrome_options.add_argument("--disable-software-rasterizer")  
    chrome_options.add_argument("--window-size=1920x1080") 

    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.tiendasjumboqaio-cmedia-integration-cencosud-0-x-galleryItem")))
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    product_cards = driver.find_elements(By.CSS_SELECTOR, "div.tiendasjumboqaio-cmedia-integration-cencosud-0-x-galleryItem")
    
    print(f"Productos encontrados: {len(product_cards)}")
    
    products:List[Product] = []
    
    for card in product_cards[:15]:
        try:
            name = card.find_element(By.CSS_SELECTOR, "span.vtex-product-summary-2-x-productBrand").text.strip()
        except Exception:
            name = "Sin nombre"
        
        try:
            price = card.find_element(By.CSS_SELECTOR, "div.tiendasjumboqaio-jumbo-minicart-2-x-cencoPriceWithoutDiscount div.tiendasjumboqaio-jumbo-minicart-2-x-price").text.strip()
        except Exception:
            price = None
        
        try:
            promo_price = card.find_element(By.CSS_SELECTOR, "div.flex.c-emphasis div.tiendasjumboqaio-jumbo-minicart-2-x-price").text.strip()
        except Exception:
            promo_price = None
        
        if price is None:
            price = promo_price
            promo_price = "Sin descuento"
        elif promo_price is None:
            promo_price = "Sin descuento"
        
        products.append({
            "name": name,
            "price": price,
            "promo_price": promo_price
        })
    print(f"Productos encontrados: {len(products)}")
    driver.quit()
    return products