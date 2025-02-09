from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field

class StoveType(Enum):
    """
    Enum that represents the stove type of the sauna
    """
    WOOD = 'wood'
    ELECTRIC = 'electric'

class LocationSchema(BaseModel):
    latitude: float = Field(..., ge=-90, le=90, description="Latitude must be between -90 and 90")
    longitude: float = Field(..., ge=-180, le=180,
                            description="Longitude must be between -180 and 180")

class SaunaSchema(BaseModel):
    """
    Common model for handling saunas in API calls
    """
    location: LocationSchema
    name: str
    sauna_id: str
    stove_type: StoveType

class CreateSaunaSchema(BaseModel):
    """
    Specifies parameters for creating a new sauna.
    Used in API calls for sauna creation.
    """
    location: LocationSchema
    name: str
    stove_type: StoveType

class ReviewSchema(BaseModel):
    """
    Schema for API responses representing a review
    """
    review_id: str
    for_sauna: str
    stars: int
    text: str
    by_user: str
    created_at: datetime

class CreateReviewSchema(BaseModel):
    """
    Used for validating the received review data
    """
    stars: int
    text: str

class GetUserSchema(BaseModel):
    """
    Schema for getting information about a user without sensitive data
    """
    username: str
    user_id: str

class CreateUserSchema(BaseModel):
    """
    Schema for user creation
    """
    username: str
    password: str
    email: str
