from starlette_admin.contrib.sqla import Admin


from app.database import engine
from app.models import User
from app.routers.admin.view import UserModelView
from app.routers.admin.auth import JSONAuthProvider

admin = Admin(
    engine=engine,
    title="Dovcha market",
    base_url="/admin",
    auth_provider=JSONAuthProvider(login_path="/login", logout_path="/logout"),
)


admin.add_view(UserModelView(User, icon="fa fa-user"))
