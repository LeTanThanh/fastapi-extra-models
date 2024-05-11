from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

class BaseUser(BaseModel):
  email: EmailStr = Field(examples = ["user@example.com"])
  username: str = Field(examples = ["USER"])
  full_name: str | None = Field(default = None, examples = ["USER"])


class UserParam(BaseUser):
  password: str = Field(examples = ["Aa@123456"])

class UserResponse(BaseUser):
  pass

class UserDb(BaseUser):
  hashed_password: str = Field(examples = ["Aa@123456"])
