from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.database import db_dep
from app.schemas import UserLoginRequest
from app.models import User
from app.utils import verify_password, generate_jwt_tokens

router = APIRouter(prefix="/auth", tags=["Auth"])

# TODO: merge into a single routers/auth.py file.


@router.post("/login/")
async def login_user(db: db_dep, login_data: UserLoginRequest):
    stmt = select(User).where(User.email == login_data.email)
    user = db.execute(stmt).scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(user.password_hash, login_data.password_hash):
        raise HTTPException(status_code=401, detail="Invalid password")

    access_token, refresh_toekn = generate_jwt_tokens(user.id)

    return {"access_token": access_token, "refresh_token": refresh_toekn}


@router.post("/logout/")
async def logout():
    # TODO: implement logout with token blacklisting
    pass


@router.post("/change/password/")
async def change_password():
    # TODO: implement password change
    pass
