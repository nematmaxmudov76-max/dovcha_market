from starlette_admin.contrib.sqla import ModelView


class UserAdmin(ModelView):
    identity = "user"
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
    exclude_fields_from_create = ["id", "created_at", "updated_at", "deleted_email"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at"]
    exclude_fields_from_list = ["password_hash", "deleted_email"]


class ShopAdmin(ModelView):
    identity = "shop"
    fields = [
        "id",
        "user",
        "image",
        "name",
        "description",
        "rating",
        "order_count",
        "created_at",
        "updated_at",
    ]
    exclude_fields_from_create = [
        "id",
        "rating",
        "order_count",
        "created_at",
        "updated_at",
    ]
    exclude_fields_from_edit = ["id", "created_at", "updated_at"]


class ImageAdmin(ModelView):
    identity = "image"
    fields = ["id", "url"]
    exclude_fields_from_create = ["id"]
    exclude_fields_from_edit = ["id"]


class ItemAdmin(ModelView):
    identity = "item"
    fields = [
        "id",
        "shop",
        "subcategory",
        "name",
        "description",
        "price",
        "quantity",
        "rating",
        "is_active",
        "created_at",
        "updated_at",
    ]
    exclude_fields_from_create = ["id", "rating", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at"]
    # related_views = [SubCategoryAdmin]  # SubCategory uchun view


class CategoryAdmin(ModelView):
    identity = "category"
    fields = ["id", "name"]
    exclude_fields_from_create = ["id"]
    exclude_fields_from_edit = ["id"]


class SubCategoryAdmin(ModelView):
    identity = "sub-category"
    fields = ["id", "category", "name"]
    exclude_fields_from_create = ["id"]
    exclude_fields_from_edit = ["id"]


class OrderAdmin(ModelView):
    identity = "order"
    fields = [
        "id",
        "user_cart",
        "user",
        "promokod",
        "location",
        "status",
        "created_at",
        "is_active",
    ]
    exclude_fields_from_create = ["id", "created_at"]
    exclude_fields_from_edit = ["id", "created_at"]


class PaymentAdmin(ModelView):
    identity = "payment"
    fields = ["id", "order", "payment_type", "amount", "status", "created_at"]
    exclude_fields_from_create = ["id", "created_at"]
    exclude_fields_from_edit = ["id", "created_at"]


class DeliveryPointAdmin(ModelView):
    identity = "delivery-point"
    fields = [
        "id",
        "region",
        "district",
        "house",
        "postal_code",
        "latitude",
        "longitude",
        "phone",
        "working_hours",
        "is_active",
        "created_at",
        "updated_at",
    ]
    exclude_fields_from_create = ["id", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at"]


class RegionAdmin(ModelView):
    identity = "region"
    fields = ["id", "name"]
    exclude_fields_from_create = ["id"]
    exclude_fields_from_edit = ["id"]


class CommentAdmin(ModelView):
    identity = "comment"
    fields = ["id", "item", "user", "text", "is_active", "created_at", "updated_at"]
    exclude_fields_from_create = ["id", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at"]


class PromokodAdmin(ModelView):
    identity = "promokod"
    fields = [
        "id",
        "discount_type",
        "discount_value",
        "expires_at",
        "usage_limit",
        "usage_count",
        "created_at",
        "updated_at",
    ]
    exclude_fields_from_create = ["id", "usage_count", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at"]


class DiscountAdmin(ModelView):
    identity = "discount"
    fields = ["id", "name", "percent", "is_active"]
    exclude_fields_from_create = ["id"]
    exclude_fields_from_edit = ["id"]


class LikeAdmin(ModelView):
    identity = "like"
    fields = ["id", "user", "item"]
    exclude_fields_from_create = ["id"]
    exclude_fields_from_edit = ["id"]


class ItemCartAdmin(ModelView):
    identity = "item_cart"
    fields = ["id", "user_cart", "item", "quantity"]
    exclude_fields_from_create = ["id"]
    exclude_fields_from_edit = ["id"]


class UserCartAdmin(ModelView):
    identity = "user-cart"
    fields = ["id", "user", "total_price"]
    exclude_fields_from_create = ["id"]
    exclude_fields_from_edit = ["id"]


class OrderItemAdmin(ModelView):
    identity = "order_item"
    fields = ["id", "order", "item", "quantity", "price_snapshot"]
    exclude_fields_from_create = ["id"]
    exclude_fields_from_edit = ["id"]


class ItemDiscountAdmin(ModelView):
    identity = "item_discount"
    fields = ["id", "item", "discount", "start_date", "end_date"]
    exclude_fields_from_create = ["id"]
    exclude_fields_from_edit = ["id"]
