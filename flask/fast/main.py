from fastapi import FastAPI, Path
from typing import Union
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello": "World"}


@app.get('/products')
def get_products(product_id: int):
    product = [
        {
            'id': 1,
            'name': 'Shampoo'
        },
        {
            'id': 2,
            'name': 'Soap'
        }
    ]
    return product

@app.get('/products/{product_id}')
def get_products(product_id: int):
    product = [
        {
            'id': 1,
            'name': 'Shampoo'
        },
        {
            'id': 2,
            'name': 'Soap'
        }
    ]
    for i in product:
        if i['id'] == product_id:
            return i

students = {
    1: {
        'name' : 'John',
        'age' : 17,
        'class': '11th'
    }
}

@app.get("/students/{student_id}")
def getStudents(student_id: int = Path(description="The ID of the student", gt=0, lt=2)):
    return students[student_id]

@app.get("/items/{item_id}")
def read_item(item_id: int = Path(description="Id of item"), product: str= None):
    return {"item_id": item_id, "product": product}

class AvailableCuisines(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"

food_items = {
    'indian' : [ "Samosa", "Dosa"],
    'american': ["Hot Dog", "Apple Pie"],
    'italian': ['Pizza', "Ravioli"]
}

@app.get("/foods/{cuisine}")
def getFoodItems(cuisine: AvailableCuisines):

    if cuisine not in food_items.keys():
        return {
            'error' : 'not found'
        }

    return food_items.get(cuisine)

class User(BaseModel):
    username: str
    password: str

@app.post("/user/login")
def userLogin(user: User):
    return {
        'username': user.username,
        'password': user.password
    }
