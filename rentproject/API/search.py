from fastapi import APIRouter, Form
import hashlib
import json
import os
from typing import Annotated
from pymongo import MongoClient
from rentproject.primitives.user import User
from rentproject.primitives.location import Property

router = APIRouter()

client = MongoClient(os.environ["RentProjectMongo"])
db = client["main"]
properties = db["Properties"]

@router.get("/search")
def search(property: Annotated[Property, Form()]) -> list[User]:
    pass