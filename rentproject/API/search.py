from fastapi import APIRouter
from rentproject.primitives.location import Property
import hashlib
import json
from pymongo import MongoClient
import keyring
from rentproject.primitives.user import User

router = APIRouter()

client = MongoClient(keyring.get_password("RentProject", "Mongo"))
db = client["main"]
properties = db["Properties"]

@router.get("/search")
def search(user_id: int, user_password: str, radius: int) -> list[Property]:
    pass