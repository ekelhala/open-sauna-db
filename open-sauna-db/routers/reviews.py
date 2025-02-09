from typing import List
from fastapi import APIRouter

from routers.schemas import ReviewSchema, CreateReviewSchema
from db.models import Review

router = APIRouter()

@router.get("/sauna/{sauna_id}", response_model=List[ReviewSchema])
def get_reviews_for_sauna(sauna_id: str):
    """
    Gets the reviews for given sauna.
    """
    # pylint: disable=no-member
    reviews = Review.objects(for_sauna=sauna_id)
    return reviews

@router.post("/sauna/{sauna_id}", response_model=ReviewSchema, status_code=201)
def create_review_for_sauna(sauna_id: str, review_data: CreateReviewSchema):
    """
    Creates a new review for a given sauna
    """

@router.get("/{review_id}", response_model=ReviewSchema)
def get_review(review_id: str):
    # pylint: disable=no-member
    return Review.objects(review_id=review_id).first()
