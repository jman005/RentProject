from fastapi import APIRouter, Form
import hashlib
import json
import os
from typing import Annotated
from pymongo import MongoClient
from rentproject.primitives.user import User
from rentproject.primitives.location import Property
from rentproject.API.user import get_user

router = APIRouter()

client = MongoClient(os.environ["RentProjectMongo"])
db = client["main"]
properties = db["Properties"]

@router.get("/search")
def search(user_id: str) -> list[Property]:
    user = get_user(user_id)
