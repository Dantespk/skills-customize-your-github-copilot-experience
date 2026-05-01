from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# TODO: Define your Pydantic models here
# Example: 
# class Item(BaseModel):
#     id: int
#     name: str
#     price: float

# TODO: Create an in-memory data storage
# Example:
# items_db = []

# TODO: Implement at least one GET endpoint
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to your REST API!"}

# TODO: Implement POST, PUT, and DELETE endpoints

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
