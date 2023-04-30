from pydantic import BaseModel, Field
from rentproject.primitives.location import Location, HousingType, Gender

'''
User JSON format:
{"gender": int, "location": {"line1": str, "postal": str, "city": str, "province": str, "line2": str},
"radius": int, "accessible": bool, "roommates": bool, "coed": bool}}
'''

class User(BaseModel):
    username: str
    password: str
    gender: Gender
    type: HousingType = Field(description="1 for condo, 2 for rent, 3 for sublet, 4 for accomodation")
    cost: int  # Daily for Accomodation, Monthly for rent/sublet, overall for Condo
    location: Location
    bedrooms: int
    bathrooms: int
    radius: int
    sqft: int
    accessible: bool
    roommates: bool
    coed: bool
