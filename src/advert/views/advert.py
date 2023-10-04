from django.http import HttpRequest
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from advert.serializers.advert_serializer import AdvertSerializer
from advert.services.advert_service import AdvertService
from advert.tasks.increment_views import increment_views
from common.exceptions import ObjectNotFoundException


class AdvertViewSet(ListModelMixin, GenericViewSet):
    serializer_class = AdvertSerializer
    permission_classes = [AllowAny]
    queryset = AdvertService.get(is_deleted=False)

    def retrieve(self, request: HttpRequest, id: str):
        queryset = self.queryset.filter(id=id).first()
        if not queryset:
            raise ObjectNotFoundException()
        increment_views.delay(queryset.id)
        serializer = self.get_serializer(queryset).data
        return Response(data=serializer)
