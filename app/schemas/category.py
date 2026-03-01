from pydantic import BaseModel


class CategoryCreateRequest(BaseModel):
    name: str


class SubcategoryCreateRequest(BaseModel):
    name: str
    category_id: int
