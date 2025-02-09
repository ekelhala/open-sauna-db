from typing import List
from datetime import datetime
from fastapi import APIRouter, HTTPException

from routers.schemas import ReviewSchema, CreateReviewSchema
from db.models import Review, Sauna

router = APIRouter()

@router.get("/sauna/{sauna_id}", response_model=List[ReviewSchema])
def get_reviews_for_sauna(sauna_id: str):
    """
    Gets the reviews for given sauna.
    """
    # pylint: disable=no-member
    if Sauna.objects(sauna_id=sauna_id):
        return Review.objects(for_sauna=sauna_id)
    raise HTTPException(status_code=404, detail=f"Sauna {sauna_id} does not exist")

@router.post("/sauna/{sauna_id}", response_model=ReviewSchema, status_code=201)
def create_review_for_sauna(sauna_id: str, review_data: CreateReviewSchema):
    """
    Creates a new review for a given sauna
    """
    # pylint: disable=no-member
    if Sauna.objects(sauna_id=sauna_id).first():
        new_review = Review(
            for_sauna=sauna_id,
            by_user="fake-id",
            stars=review_data.stars,
            text=review_data.text,
            created_at=datetime.now()
        )
        new_review.save()
        return new_review
    raise HTTPException(status_code=404, detail=f"Sauna {sauna_id} does not exist")

@router.get("/{review_id}", response_model=ReviewSchema)
def get_review(review_id: str):
    # pylint: disable=no-member
    return Review.objects(review_id=review_id).first()
