from uuid import uuid4

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from pytz import timezone

tz = timezone(settings.TIME_ZONE)


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        unique=True,
        verbose_name=_("ID"),
    )
    is_deleted = models.BooleanField(default=False, verbose_name=_("удаленный?"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("дата создания")
    )

    def get_date(self):
        return self.created_at.astimezone(tz).date()

    def get_hour(self):
        return self.created_at.astimezone(tz).time()

    class Meta:
        abstract = True
