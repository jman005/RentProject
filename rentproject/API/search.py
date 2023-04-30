from fastapi import APIRouter
import hashlib
import json
import os
from pymongo import MongoClient
from rentproject.primitives.user import User
from rentproject.primitives.location import Property

router = APIRouter()

client = MongoClient(os.environ["RentProjectMongo"])
db = client["main"]
properties = db["Properties"]

@router.get("/search")
def search(property: Property) -> list[User]:

    pass