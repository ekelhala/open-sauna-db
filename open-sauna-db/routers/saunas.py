from typing import List
from fastapi import APIRouter
from models import Sauna, CreateSauna

router = APIRouter()

# Get
@router.get("/", response_model=List[Sauna])
def get_all_saunas():
    """Returns all saunas in the database."""

@router.get("/{sauna_id}", response_model=Sauna)
def get_sauna(sauna_id: int):
    """ Get a specific sauna by supplying an id."""

#Post
@router.post("/", response_model=Sauna)
def create_sauna(sauna: CreateSauna):
    """Creates a new sauna and inserts it into the database."""
