from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class City(BaseModel):
    name = models.CharField(
        max_length=150, blank=False, null=False, verbose_name=_("City")
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "city"
        verbose_name = _("City")
        verbose_name_plural = _("Cities")


class Category(BaseModel):
    name = models.CharField(
        max_length=150, blank=False, null=False, verbose_name=_("Category name")
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "category"
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Advert(BaseModel):
    title = models.CharField(
        max_length=250, blank=False, null=False, verbose_name=_("Title")
    )
    description = models.TextField()
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("City")
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name=_("Category"),
    )
    views = models.PositiveIntegerField(default=0, verbose_name=_("Views count"))

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "advert"
        verbose_name = _("Advert")
        verbose_name_plural = _("Adverts")
