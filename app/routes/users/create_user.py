from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter()

class User(BaseModel):
  name: str
  email: EmailStr
  password: str

@router.post("/users", tags=["usuários"])
async def create_user(user: User) -> dict:
  return { "message": "User created successfully", "user": user }