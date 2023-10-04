from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from advert.serializers.category_serializer import CategorySerializer
from advert.services.advert_service import CategoryService


class CategoryAPIView(ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    queryset = CategoryService.get(is_deleted=False)
