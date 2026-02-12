from django.db import models

from utils.mixins import SoftDeleteMixin


class Book(SoftDeleteMixin, models.Model):
    title = models.CharField(max_length=64, blank=False)
    edition = models.PositiveSmallIntegerField(default=1)
    published_date = models.DateField(null=False, blank=False)
    author = models.ForeignKey('authors.Author', on_delete=models.CASCADE, related_name='books')
    categories = models.ManyToManyField('categories.Category', related_name='books')
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    deleted_at = models.DateTimeField(null=True, editable=False)

    class Meta:
        db_table = 'books'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
