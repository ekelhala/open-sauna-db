from typing import List
from fastapi import APIRouter, HTTPException
from models import SaunaScheme, CreateSaunaScheme
from db.models import Sauna

router = APIRouter()

# Get
@router.get("/", response_model=List[SaunaScheme])
def get_all_saunas():
    """Returns all saunas in the database."""
    # pylint: disable=no-member
    saunas = Sauna.objects()
    return [sauna.to_dict() for sauna in saunas]

@router.get("/{sauna_id}", response_model=SaunaScheme)
def get_sauna(sauna_id: str):
    """ Get a specific sauna by supplying an id."""
    # pylint: disable=no-member
    sauna = Sauna.objects(sauna_id=sauna_id).first()
    return sauna.to_dict()

#Post
@router.post("/", response_model=SaunaScheme, status_code=201)
def create_sauna(sauna: CreateSaunaScheme):
    """Creates a new sauna and inserts it into the database."""
    try:
        new_sauna = Sauna(
                            name=sauna.name,
                            location=[sauna.location.longitude, sauna.location.latitude],
                            stove_type=sauna.stove_type.value)
        new_sauna.save()
        return new_sauna.to_dict()
    except Exception as e:
        print(e)
        raise HTTPException(400, "Invalid request") from e
