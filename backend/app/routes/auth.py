import select
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.user import User

from backend.app.schemas.user import UserCreate

auth_router = APIRouter(tags=["auth"])

@auth_router.post("/register")
def register(
    user: UserCreate,
    db: Session=Depends(get_db)
):
    
    
    return {
        "email": user.email,
        "message": 'registration successfull'
    }