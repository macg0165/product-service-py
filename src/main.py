from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

products = [{"id": 1, "name": "Dog Food", "price": 19.99}, {"id": 2, "name": "Cat Food", "price": 34.99}, {"id": 3, "name": "Bird Seeds", "price": 10.99}]

@app.get("/products")
def get_products():
    return products

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
)