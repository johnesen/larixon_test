from django.urls import path

from advert.views.advert import AdvertViewSet

urlpatterns = [
    path("", AdvertViewSet.as_view({"get": "list"})),
    path("<uuid:id>", AdvertViewSet.as_view({"get": "retrieve"})),
]
