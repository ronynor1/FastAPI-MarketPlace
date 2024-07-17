"""
This is the entry point of running the project
"""
from dotenv import load_dotenv
load_dotenv()
import uvicorn
from fastapi import FastAPI
from src.features.users.route import users_router
from src.features.product_management.route import products_router
from src.features.shopping_cart.route import shopping_router
from src.features.order_management.route import orders_router


app = FastAPI()

app.include_router(users_router)
app.include_router(products_router)
app.include_router(shopping_router)
app.include_router(orders_router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
