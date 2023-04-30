from fastapi import APIRouter, Form
import hashlib
import json
import os
from typing import Annotated, Any
from pymongo import MongoClient, GEO2D
from pydantic.tools import parse_obj_as
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
    properties_list = []
    for property in properties.find({"coordinates": {"$near": {
            "$geometry" : {
               "type" : "Point" ,
               "coordinates" : [user.location.longitude, user.location.latitude] },
            "$maxDistance": 10000000
          }}}).limit(5):
        property.pop("_id")
        properties_list.append(property)
    return properties_list