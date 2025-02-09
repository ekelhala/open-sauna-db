from typing import List
from fastapi import APIRouter, HTTPException
from mongoengine import ValidationError

from routers.schemas import SaunaSchema, CreateSaunaSchema
from db.models import Sauna

router = APIRouter()

# Get
@router.get("/", response_model=List[SaunaSchema])
def get_all_saunas():
    """Returns all saunas in the database."""
    # pylint: disable=no-member
    saunas = Sauna.objects()
    return [sauna.to_dict() for sauna in saunas]

@router.get("/{sauna_id}", response_model=SaunaSchema)
def get_sauna(sauna_id: str):
    """ Get a specific sauna by supplying an id."""
    # pylint: disable=no-member
    sauna = Sauna.objects(sauna_id=sauna_id).first()
    return sauna.to_dict()

#Post
@router.post("/", response_model=SaunaSchema, status_code=201)
def create_sauna(sauna: CreateSaunaSchema):
    """Creates a new sauna and inserts it into the database."""
    try:
        new_sauna = Sauna(
                            name=sauna.name,
                            location=[sauna.location.longitude, sauna.location.latitude],
                            stove_type=sauna.stove_type.value)
        new_sauna.save()
        return new_sauna.to_dict()
    except ValidationError as e:
        raise HTTPException(400, "Invalid request") from e
