import re

from datetime import date

from rest_framework import serializers

from authors.serializers import AuthorSerializer
from authors.models import Author

from categories.serializers import CategorySerializer
from categories.models import Category

from utils import regex_patterns as rgx

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='book-detail')

    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all_without_deleted(),
        write_only=True,
        source='author'
    )

    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all_without_deleted(),
        write_only=True,
        source='categories',
        many=True
    )

    class Meta:
        model = Book
        fields = ['id', 'url', 'title', 'edition', 'published_date', 'price', 'author', 'author_id', 'categories',
                  'category_ids']
        read_only_fields = ['id']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Book.objects.all_without_deleted(),
                fields=['title', 'edition'],
                message='A book with this title and edition already exists.'
            )
        ]

    def validate_title(self, value: str):
        book_title = ' '.join(value.strip().split()).title()

        if len(book_title) < 3:
            raise serializers.ValidationError('title must be at least 3 characters long.')

        if not re.match(rgx.VALID_TITLE, book_title):
            raise serializers.ValidationError('title must contain English letters, spaces and numbers.')

        return book_title

    def validate_edition(self, value):
        if not isinstance(value, int) or int(value) <= 0:
            raise serializers.ValidationError('edition must be a positive number.')

        return value

    def validate_published_date(self, value: date):
        today = date.today()

        if value >= today:
            raise serializers.ValidationError('published date cannot be today or in the future.')

        return value
