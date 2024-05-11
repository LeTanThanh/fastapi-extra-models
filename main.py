from fastapi import FastAPI
from fastapi import Body

from typing import Annotated

from models.user import UserParam
from models.user import UserResponse
from models.user import UserDb

from utils.password import hash_password
from crud.user import save_user

app = FastAPI()

# Multiple models
@app.post("/users", response_model = UserResponse)
async def create_user(user: Annotated[UserParam, Body(embed = True)]) -> UserResponse:
  user_db: UserDb = save_user(user = user)
  return UserResponse(**user_db.model_dump())
