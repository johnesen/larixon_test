from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException


class ObjectNotFoundException(APIException):
    status_code = 404
    default_detail = _("Object not found.")
    default_code = "notFound"
