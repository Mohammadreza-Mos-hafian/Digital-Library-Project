from django.db import models

from utils.mixins import SoftDeleteMixin


class Category(SoftDeleteMixin, models.Model):
    name = models.CharField(max_length=64, blank=False, unique=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    deleted_at = models.DateTimeField(null=True, editable=False)

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
