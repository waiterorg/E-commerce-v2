from django.contrib import admin

from . import models
from .tasks import promotion_prices


class ProductOnPromotion(admin.StackedInline):
    model = models.Promotion.products_on_promotion.through
    extra = 4
    raw_id_fields = ("product_inventory_id",)


class PromotionList(admin.ModelAdmin):
    model = models.Promotion
    inlines = (ProductOnPromotion,)
    list_display = ("name", "is_active", "promo_start", "promo_end")

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        promotion_prices.delay(obj.promo_reduction, obj.id)


admin.site.register(models.Promotion, PromotionList)
admin.site.register(models.PromoType)
admin.site.register(models.Coupon)
