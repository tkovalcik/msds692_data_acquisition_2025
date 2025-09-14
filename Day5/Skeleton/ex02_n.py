from fastapi import FastAPI
from pydantic import BaseModel


# 1. Create a FastAPI App Instance
app = FastAPI()
items = {}  # In-memory database


class Student(BaseModel):
    name: str
    email: str
    age: int | None = None

@app.post("/add_student")
def create_student(student: Student):
    return {"name":student.name,
            "email":student.email,
            "age":student.age}

# requests.post("url/add_student",
#               data = {"name": "PJ",
#                       "email": "pjmask@gmail.com"})



@app.post("/add_items/")
def create_item(item : Item):
    items[item.name] = item
    return {"message":"Item received", "item":item}

@app.get("/list_items")
def list_all():
    return {"items": items}

