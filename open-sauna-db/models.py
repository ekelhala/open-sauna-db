from pydantic import BaseModel

class Sauna(BaseModel):
    """
    Common model for handling saunas in API calls
    """
    location_latitude: str
    location_longitude: str
    name: str
    id: int
