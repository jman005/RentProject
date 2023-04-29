from pydantic import BaseModel
from enum import Enum

class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3

class HousingType(Enum):
    CONDO = 1
    RENT = 2
    SUBLET = 3
    ACCOMODATION: 4

class Location(BaseModel):
    longitude: int = 0.0
    latitude: int = 0.0
    line1: str = ""
    postal: str = ""
    city: str = ""
    province: str = ""
    line2: str = ""

class Property(BaseModel):
    type: HousingType
    cost: int # Daily for Accomodation, Monthly for rent/sublet, overall for Condo
    location: Location
    bedrooms: int
    bathrooms: int
    sqft: int
    accessible: bool
    roommates: bool
    coed: bool
    gender_restricted: Gender | None = None


