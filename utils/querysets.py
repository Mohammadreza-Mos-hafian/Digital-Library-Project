from django.db import models
from django.utils import timezone


class SoftDeleteQuerySet(models.QuerySet):
    def soft_delete(self):
        return super().update(
            is_deleted=True,
            deleted_at=timezone.now()
        )

    def restore(self):
        return super().update(
            is_deleted=False,
            deleted_at=None
        )

    def deleted(self):
        return self.filter(is_deleted=True)

    def all_without_deleted(self):
        return self.filter(is_deleted=False)
