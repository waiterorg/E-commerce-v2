from ecommerce.inventory.models import Category
from ninja import ModelSchema


class CategorySchema(ModelSchema):
    class Config:
        model = Category
        model_fields = ["name", "slug"]
