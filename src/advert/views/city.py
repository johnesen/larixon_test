from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from advert.serializers.category_serializer import CategorySerializer
from advert.services.advert_service import CityService


class CityAPIView(ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    queryset = CityService.get(is_deleted=False)
