"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from ecommerce.api.views import (
    CategoryList,
    ProductByCategory,
    ProductInventoryByWebId,
)
from ecommerce.search.views import SearchProductInventory

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/search/<str:query>/", SearchProductInventory.as_view()),
    path("api/inventory/category/all/", CategoryList.as_view()),
    path(
        "api/inventory/products/category/<str:query>/",
        ProductByCategory.as_view(),
    ),
    path("api/inventory/<int:query>/", ProductInventoryByWebId.as_view()),
]
