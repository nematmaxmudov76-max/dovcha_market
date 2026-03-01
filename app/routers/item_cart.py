from fastapi import APIRouter

from app.database import db_dep
from app.schemas import current_user_jwt_dep, ItemCartsIn
from app.models import ItemCart

router = APIRouter(prefix="/item_cart", tags=["ItemCart"])


@router.post("/create")
async def item_cart_create(
    session: db_dep, current_user: current_user_jwt_dep, create_data: ItemCartsIn
):
    # TODO: move to users, with name /cart/add/
    item_cart = ItemCart(
        user_cart_id=create_data.user_cart_id, item_id=create_data.item_id
    )

    session.add(item_cart)
    session.commit()
    session.refresh(item_cart)

    return item_cart
