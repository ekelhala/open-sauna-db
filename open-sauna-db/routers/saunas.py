from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models import Sauna, CreateSauna
from db import models

router = APIRouter()

# Get
@router.get("/", response_model=List[Sauna])
def get_all_saunas():
    """Returns all saunas in the database."""
    saunas = models.Sauna.objects()
    return saunas

@router.get("/{sauna_id}", response_model=Sauna)
def get_sauna(sauna_id: int):
    """ Get a specific sauna by supplying an id."""
    sauna = models.Sauna.objects(sauna_id=sauna_id).first()
    return sauna

#Post
@router.post("/", response_model=Sauna)
def create_sauna(sauna: CreateSauna):
    """Creates a new sauna and inserts it into the database."""
    try:
        new_sauna = models.Sauna(
                                name=sauna.name,
                                location=[sauna.location.longitude, sauna.location.latitude],
                                stove_type=sauna.stove_type.value)
        new_sauna.save()
        return JSONResponse(new_sauna.to_json(), 201)
    except Exception:
        return JSONResponse({"error": "Invalid request"}, 400)
