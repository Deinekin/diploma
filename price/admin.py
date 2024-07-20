from django.contrib import admin

from price.models import Price


@admin.register(Price)
class CourseAdmin(admin.ModelAdmin):
    list_filter = (
        "user",
        "price",
        "goods",
        "taxes",
        "bank_taxes",
        "seller_taxes",
        "self_profit",
        "total_price",
    )
