from starlette_admin.contrib.sqla import ModelView


class UserModelView(ModelView):
    fields = [
        "id",
        "email",
        "password_hash",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_admin",
        "is_deleted",
        "deleted_email",
        "created_at",
        "updated_at",
    ]
    exclude_fields_from_create = ["id", "deleted_email", "created_at", "updated_at"]
    exclude_fields_from_list = ["password_hash", "deleted_email"]
    exclude_fields_from_edit = ["created_at", "updated_at", "id"]
