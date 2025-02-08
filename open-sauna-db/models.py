from enum import Enum
from pydantic import BaseModel
from pydantic_extra_types.coordinate import Coordinate

class StoveType(Enum):
    """
    Enum that represents the stove type of the sauna
    """
    WOOD = 'wood'
    ELECTRIC = 'electric'

class Sauna(BaseModel):
    """
    Common model for handling saunas in API calls
    """
    location: Coordinate
    name: str
    sauna_id: int
    stove_type: StoveType

class CreateSauna(BaseModel):
    """
    Specifies parameters for creating a new sauna.
    Used in API calls for sauna creation.
    """
    location: Coordinate
    name: str
    stove_type: StoveType
