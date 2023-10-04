from django.urls import include, path

urlpatterns = [
    path("advert/", include("advert.routes.advert_routes"), name="main-advert"),
    path("category/", include("advert.routes.category_routes"), name="main-category"),
    path("city/", include("advert.routes.city_routes"), name="main-city"),
]
