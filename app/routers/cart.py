from fastapi import APIRouter

from app.database import db_dep
from app.schemas import current_user_jwt_dep, UserCartCreateResponset
from app.models import UserCart


router = APIRouter(prefix="/cart", tags=["UserCart"])


@router.post("/create", response_model=UserCartCreateResponset, deprecated=True)
async def create_cart(session: db_dep, current_user: current_user_jwt_dep):
    # TODO: remove this API
    # TODO: user cart yaratish registerda bitta session ichida bo'ladi.
    # TODO: Userda faqat 1 ta cart bo'lishi kerak

    cart = UserCart(user_id=current_user.id)

    session.add(cart)
    session.commit()
    session.refresh(cart)

    return cart
