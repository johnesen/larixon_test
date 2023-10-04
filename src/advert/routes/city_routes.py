from django.urls import include, path

from advert.views.city import CityAPIView

urlpatterns = [
    path("", CityAPIView.as_view()),
]
