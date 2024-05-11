from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

class UserParam(BaseModel):
  email: EmailStr = Field(examples = ["user@example.com"])
  password: str = Field(examples = ["Aa@123456"])
  username: str = Field(examples = ["USER"])
  full_name: str | None = Field(default = None, examples = ["USER"])

class UserResponse(BaseModel):
  email: EmailStr = Field(examples = ["user@example.com"])
  username: str = Field(examples = ["USER"])
  full_name: str | None = Field(default = None, examples = ["USER"])

class UserDb(BaseModel):
  email: EmailStr = Field(examples = ["user@example.com"])
  hashed_password: str = Field(examples = ["Aa@123456"])
  username: str = Field(examples = ["USER"])
  full_name: str | None = Field(default = None, examples = ["USER"])
