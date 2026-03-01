from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from app.database import db_dep
from app.models import Shop
from app.schemas import current_user_jwt_dep, ShopCreateResponse, ShopCreateRequest

router = APIRouter(prefix="/shop", tags=["Shop"])


@router.post("/create", response_model=ShopCreateResponse)
async def shop_create(
    db: db_dep, create_data: ShopCreateRequest, current_user: current_user_jwt_dep
):
    if (
        not (current_user.is_staff or current_user.is_admin)
        and not current_user.is_active
    ):
        raise HTTPException(status_code=403, detail="Sizda do'kon qo'sha olmaysiz!!")

    shop = Shop(
        user_id=current_user.id,
        image_id=create_data.image_id,
        name=create_data.name,
        description=create_data.description,
    )
    db.add(shop)
    db.commit()
    db.refresh(shop)

    return shop


@router.get("/list", response_model=list[ShopCreateResponse])
async def shop_list(db: db_dep):
    stmt = select(Shop)
    shops = db.execute(stmt).scalars().all()

    return shops
