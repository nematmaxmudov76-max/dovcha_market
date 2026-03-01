from fastapi import APIRouter, HTTPException
from sqlalchemy import select


from app.database import db_dep
from app.models import Item
from app.schemas import current_user_jwt_dep, ItemCreateRequest, ItemCreateResponse


router = APIRouter(prefix="/item", tags=["Item"])


@router.post("/create", response_model=ItemCreateResponse)
async def item_create(
    session: db_dep, current_user: current_user_jwt_dep, create_data: ItemCreateRequest
):
    # TODO: remove admin check. Users can also add
    # TODO: check if user has any shop. Link product to shop
    if (
        not current_user.is_active
        or not current_user.is_admin
        or not current_user.is_staff
    ):
        raise HTTPException(status_code=403, detail="sizda bunday huquq yuq!")

    item = Item(
        shop_id=create_data.shop_id,
        subcategory_id=create_data.subcategory_id,
        name=create_data.name,
        price=create_data.price,
        description=create_data.description,
        quantity=create_data.quantity,
    )

    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.get("/list", response_model=list[ItemCreateResponse])
async def item_list(session: db_dep, current_user: current_user_jwt_dep):
    # TODO: fix - items should be ordered in some way (rating, price, name query paramda berish)
    # TODO: filter by is_active
    # TODO: add pagination

    if not current_user.is_active:
        raise HTTPException(status_code=404, detail="User not found.")

    stmt = select(Item)
    res = session.execute(stmt).scalars()

    return res


@router.get("/one", response_model=ItemCreateResponse)
async def item_one(session: db_dep, current_user: current_user_jwt_dep, item_id: int):
    # TODO: move item_id to path param
    # TODO: so only admins can see the item detail?
    # TODO: admin checks should be in dependency
    if (
        not current_user.is_active
        or not current_user.is_admin
        or not current_user.is_staff
    ):
        raise HTTPException(status_code=403, detail="user is not active ")

    stmt = select(Item).where(Item.id == item_id)
    res = session.execute(stmt).scalars().first()
    if not res:
        raise HTTPException(status_code=404, detail="Item not found")

    return res


@router.get("/filter", response_model=list[ItemCreateResponse])
async def item_search(db: db_dep, title):
    # TODO: remove this API. Filter occurs in list
    stmt = select(Item).where(Item.name.ilike(f"%{title}%"))
    item = db.execute(stmt).scalars().all()

    return item


@router.get(
    "/search",
    response_model=list[ItemCreateResponse],
    summary="bi itemni category,is_active va name bo;yicha qidirish!!",
)
async def search(
    db: db_dep, name: str | None, subcategory_id: int | None, is_active: bool | None
):
    # TODO: remove this API - search occurs in list

    if is_active is not None:
        stmt = select(Item).where(Item.is_active == is_active)
    if name:
        stmt = select(Item).where(Item.name.ilike(f"%{name}%"))

    if subcategory_id:
        stmt = select(Item).where(Item.subcategory_id == subcategory_id)

    item = db.execute(stmt).scalars().all()

    return item
