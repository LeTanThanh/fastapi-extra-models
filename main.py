from fastapi import FastAPI
from fastapi import Body
from fastapi import Path

from typing import Annotated
from typing import Union

from models.user import UserParam
from models.user import UserResponse
from models.user import UserDb

from models.item import CarItem
from models.item import PlaneItem

from utils.password import hash_password
from crud.user import save_user

app = FastAPI()

# Multiple models
@app.post("/users", response_model = UserResponse)
async def create_user(user: Annotated[UserParam, Body(embed = True)]) -> UserResponse:
  user_db: UserDb = save_user(user = user)
  return UserResponse(**user_db.model_dump())

# Union or anyOf
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

@app.get("/items/{id}", response_model = Union[PlaneItem, CarItem])
async def read_items(id: Annotated[str, Path()]) -> PlaneItem | CarItem:
  return items[id]
