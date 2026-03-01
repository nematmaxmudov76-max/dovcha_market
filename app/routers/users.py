from fastapi import APIRouter

from app.schemas import UserProfilResponse, current_user_jwt_dep
# TODO: dependencies.py should be in app/ folder

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserProfilResponse)
async def user_profile(current_user: current_user_jwt_dep):
    return current_user


@router.get("/me/update/")
async def profile_update():
    # TODO: update profile
    pass


@router.post("/avatar/upload/")
async def avatar_upload():
    # TODO: avatar upload API
    pass


@router.delete("/avatar/delete/")
async def avatar_delete():
    # TODO: avatar delete API
    pass


@router.post("/me/deactivate/")
async def deactivate_account():
    # TODO: deactivate account. Set is_deleted=True, change email to preserve unique=True
    pass
