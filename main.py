from fastapi import FastAPI
from fastapi import Body
from fastapi import Path

from typing import Annotated

from models.user import UserParam
from models.user import UserResponse
from models.user import UserDb

from models.item import CarItem
from models.item import PlaneItem
from models.item import Item

from utils.password import hash_password
from crud.user import save_user

app = FastAPI()

# Multiple models
@app.post("/users", response_model = UserResponse)
async def create_user(user: Annotated[UserParam, Body(embed = True)]) -> UserResponse:
  user_db: UserDb = save_user(user = user)
  return UserResponse(**user_db.model_dump())

# Union or anyOf
@app.get("/items/{id}", response_model = PlaneItem | CarItem)
async def read_items(id: Annotated[str, Path()]) -> PlaneItem | CarItem:
  items = {
    "car": {
      "description": "All my friends drive a low rider",
      "type": "car"
    },
    "plane": {
      "description": "Music is my aeroplane, it's my aeroplane",
      "type": "plane",
      "size": 5
    }
  }
  return items[id]

# List of models
@app.get("/items", response_model=list[Item])
async def read_items() -> list[Item]:
  items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
  ]
  return items

# Response with arbitrary dict
@app.get("/keyword_weights", response_model = dict[str, float])
def read_keyword_weights() -> dict[str, float]:
  return {"foo": 2.3, "bar": 3.4}
