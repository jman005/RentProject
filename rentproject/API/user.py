from fastapi import APIRouter
import hashlib
import json
from pymongo import MongoClient
import keyring
from rentproject.primitives.user import User

router = APIRouter()

client = MongoClient(keyring.get_password("RentProject", "Mongo"))
db = client["main"]
users = db["Users"]


@router.post("/create_user")
def create_user(user_id: str, user_password: str, user_data: User):
    hashword = hashlib.sha256()
    hashword.update(user_password.encode())
    users.insert_one({
        "user_id": user_id,
        "user_password": hashword.hexdigest(),
        "user_data": json.loads(user_data.json())
    })

@router.post("/update_user")
def update_user(user_id: str, user_password: str, user_data: User):
    hashword = hashlib.sha256()
    hashword.update(user_password.encode())
    collection = client['Users']
    user = {"user_id": hashword.hexdigest()}
    users.update_one(user, {
        "user_id": user_id,
        "user_password": hashword.hexdigest(),
        "user_data": json.loads(user_data.json())
    })