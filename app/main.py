from fastapi import FastAPI

from app.routers.admin import admin
from app.routers import (
    auth_router,
    item_router,
    shop_router,
    cart_router,
    item_cart_router,
    category_router,
    subcategory_router,
)
from app.middleware import DBSessionMiddleware

app = FastAPI(
    title="DOVCHA MARKET ", description="Dovcha Market Uzum marketning copy versiyasi"
)


app.include_router(auth_router)
app.include_router(item_router)
app.include_router(shop_router)
app.include_router(cart_router)
app.include_router(item_cart_router)
app.include_router(category_router)
app.include_router(subcategory_router)

app.add_middleware(DBSessionMiddleware)


admin.mount_to(app=app)
