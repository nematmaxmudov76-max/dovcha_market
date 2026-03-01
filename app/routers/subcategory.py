from fastapi import APIRouter


from app.database import db_dep
from app.models import SubCategory
from app.schemas import current_user_jwt_dep, SubcategoryCreateRequest


router = APIRouter(prefix="/subcategory", tags=["SubCategory"])


@router.post("/create")
async def sub_category_create(
    session: db_dep, current_user: current_user_jwt_dep, data: SubcategoryCreateRequest
):
    # TODO: remove this API, only admin does it
    category = SubCategory(name=data.name, category_id=data.category_id)

    session.add(category)
    session.commit()
    session.refresh(category)
    return category
