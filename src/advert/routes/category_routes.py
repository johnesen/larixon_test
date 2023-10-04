from django.urls import include, path

from advert.views.category import CategoryAPIView

urlpatterns = [
    path("", CategoryAPIView.as_view()),
]
