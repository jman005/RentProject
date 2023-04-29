from fastapi import APIRouter
from rentproject.primitives.location import Property

router = APIRouter()

@router.get("/search")
def search(user_id: int, user_password: str, radius: int) -> list[Property]:
    pass