from enum import Enum
from pydantic import BaseModel, Field
from typing import List

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

class SaunaScheme(BaseModel):
    """
    Common model for handling saunas in API calls
    """
    location: LocationSchema
    name: str
    sauna_id: str
    stove_type: StoveType

class CreateSaunaScheme(BaseModel):
    """
    Specifies parameters for creating a new sauna.
    Used in API calls for sauna creation.
    """
    location: LocationSchema
    name: str
    stove_type: StoveType
