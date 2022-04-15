from typing import List

from ecommerce.inventory.models import Category
from ninja import NinjaAPI
from .schema import CategorySchema

api = NinjaAPI()


@api.get("/inventory/category/", response=List[CategorySchema])
def category_list(request):
    qs = Category.objects.all()
    return qs
