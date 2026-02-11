from django.db import models

from . import querysets


class SoftDeleteManager(models.Manager.from_queryset(querysets.SoftDeleteQuerySet)):
    def get_queryset(self):
        return super().get_queryset()
