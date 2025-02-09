from typing import List
from fastapi import APIRouter

from routers.schemas import ReviewSchema, CreateReviewSchema

router = APIRouter()

@router.get("/{sauna_id}", response_model=List[ReviewSchema])
def get_review_for_sauna(sauna_id: str):
    """
    Gets the reviews for given sauna.
    """

@router.post("/{sauna_id}", response_model=ReviewSchema, status_code=201)
def create_review_for_sauna(sauna_id: str, review_data: CreateReviewSchema):
    """
    Creates a new review for a given sauna
    """
