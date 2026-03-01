from fastapi import APIRouter


from app.database import db_dep
from app.models import Category
from app.schemas import (
    current_user_jwt_dep,
    CategoryCreateRequest,
)


router = APIRouter(prefix="/category", tags=["Category"])


@router.post("/create")
async def category_create(
    session: db_dep, current_user: current_user_jwt_dep, data: CategoryCreateRequest
):
    # TODO: remove this API. Only admin creates
    category = Category(name=data.name)

    session.add(category)
    session.commit()
    session.refresh(category)
    return category
