from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def intro():
    return {"Hello": "World"}

@app.get("/hello")
def custom_intro(name: str | None = None):
    if name:
        return {"message": f"Hello {name}"}
    return {"message": "hello stranger"}

@app.get("/hello/{name}")
def custom_intro(name: str):
    return {"message": f"Hello {name}"}



@app.get("/items/{item_id}")
def read_item_w_path_param(item_id):
    return {"item_id": item_id}