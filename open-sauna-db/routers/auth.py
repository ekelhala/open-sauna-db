"""
Module implementing authentication logic
"""
from fastapi import APIRouter

from routers.schemas import AuthenticateUserSchema

router = APIRouter()

@router.post("/")
def login_user(user: AuthenticateUserSchema):
    """
    Checks given credentials and returns authentication token if successful
    """
