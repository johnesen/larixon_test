from advert.models import Advert, Category, City


class AdvertService:
    model = Advert

    @classmethod
    def get(cls, **filters):
        return (
            cls.model.objects.filter(**filters)
            .select_related("city", "category")
            .order_by("-created_at")
        )


class CategoryService:
    model = Category

    @classmethod
    def get(cls, **filters):
        return cls.model.objects.filter(**filters).order_by("-created_at")


class CityService:
    model = City

    @classmethod
    def get(cls, **filters):
        return cls.model.objects.filter(**filters).order_by("-created_at")
