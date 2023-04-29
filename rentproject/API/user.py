from fastapi import APIRouter
from rentproject.primitives.user import User

router = APIRouter()

@router.post("/create_user")
def create_user(user_id: str, user_password: str, user_data: User):
    pass

@router.post("/update_user")
def update_user(user_id: str, user_password: str, user_data: User):
    pass