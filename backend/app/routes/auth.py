from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database.db import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.security.password import hash_password, verify_password
from app.security.jwt import create_access_token
from app.schemas.auth import UserLogin, TokenResponse


auth_router = APIRouter(tags=["auth"])


@auth_router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    statement = select(User).where(User.email == user.email)
    result = db.execute(statement)
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )

    hashed_password = hash_password(user.password)

    new_user = User(
        email=user.email,
        hashed_password=hashed_password,
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

    except Exception:
        db.rollback()
        raise

    return UserResponse(
        id=new_user.id,
        email=new_user.email,
        message="Registration Successful"
    )


@auth_router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=TokenResponse
)
def login(
    user: UserLogin,
    db: Session = Depends(get_db),
):
    statement = select(User).where(User.email == user.email)
    result = db.execute(statement)
    db_user = result.scalar_one_or_none()

    if (
        db_user is None
        or not verify_password(
            user.password,
            db_user.hashed_password,
        )
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        {
            "sub": str(db_user.id),
        }
    )

    return TokenResponse(
        access_token=access_token,
        token_type="bearer"
    )