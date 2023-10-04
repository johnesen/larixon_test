from __future__ import absolute_import, unicode_literals

from advert.models import Advert
from config.celery import app


@app.task
def increment_views(advert_id):
    advert = Advert.objects.filter(id=advert_id).first()
    if advert:
        advert.views += 1
        advert.save()
    return True
