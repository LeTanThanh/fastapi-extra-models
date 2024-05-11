from models.user import UserParam
from models.user import UserDb

from utils.password import hash_password

def save_user(user: UserParam) -> UserDb:
  hash_passworded = hash_password(password = user.password)
  user_db = UserDb(**user.model_dump(), hashed_password = hash_passworded)
  return user_db
