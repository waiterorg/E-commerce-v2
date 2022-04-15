from ecommerce.inventory.models import Category, Product
from ninja import ModelSchema


class CategorySchema(ModelSchema):
    class Config:
        model = Category
        model_fields = ["name", "slug"]


class ProductSchema(ModelSchema):
    class Config:
        model = Product
        model_fields = [
            "name",
            "web_id",
        ]
