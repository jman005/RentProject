from fastapi import APIRouter, Form, HTTPException
import hashlib
import json
from pydantic.tools import parse_obj_as
from pymongo import MongoClient
import os
from typing import Annotated, Union
from rentproject.primitives.user import User, UserLogin

router = APIRouter()

client = MongoClient(os.environ["RentProjectMongo"])
db = client["main"]
users = db["Users"]

def get_user(user_id: str) -> Union[User, None]:
    user_data = users.find_one({"username": user_id})
    if not user_data:
        return None
    return parse_obj_as(User, user_data)


@router.post("/create_user")
def create_user(user_data: User):
    is_user = get_user(user_data.username)
    if is_user:
        raise HTTPException(status_code=403, detail="Username taken")
    hashword = hashlib.sha256()
    hashword.update(user_data.password.encode())
    user_data.password = hashword.hexdigest()
    users.insert_one(json.loads(user_data.json()))

@router.post("/update_user")
def update_user(user_id: str, user_password: str, user_data: User):
    hashword = hashlib.sha256()
    hashword.update(user_password.encode())
    user = {"user_id": hashword.hexdigest()}
    users.update_one(user, {
        "user_id": user_id,
        "user_password": hashword.hexdigest(),
        "user_data": json.loads(user_data.json())
    })


@router.post("/login")
def create_user(user_data: UserLogin):
    user = get_user(user_data.username)
    if not user:
        raise HTTPException(status_code=404, detail="Unknown Username")
    hashword = hashlib.sha256()
    hashword.update(user_data.password.encode())
    if hashword.hexdigest() != user.password:
        raise HTTPException(status_code=403, detail="Incorrect Password")
