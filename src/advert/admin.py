from django.contrib import admin

from advert.models import Advert, Category, City

admin.site.register(Category)
admin.site.register(City)


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "city", "views"]
    fields = [
        "title",
        "description",
        "category",
        "city",
        "views",
        "is_deleted",
        "created_at",
    ]
    readonly_fields = ["views", "created_at"]
