from pydantic import BaseModel
from pydantic import Field

class BaseItem(BaseModel):
  description: str = Field()
  type: str

class CarItem(BaseItem):
  type: str = Field(default = "car")

class PlaneItem(BaseItem):
  type: str = Field(default = "plane")
  size: int = Field()
