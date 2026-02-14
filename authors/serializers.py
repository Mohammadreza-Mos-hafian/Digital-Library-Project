import re

from rest_framework import serializers

from .models import Author

from utils import functions


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']
        read_only_fields = ['id']

    def validate_name(self, value: str):
        author_name = ' '.join(value.strip().split()).capitalize()

        if len(author_name) < 3:
            raise serializers.ValidationError('author name must be at least 3 characters long.')

        if not re.match(r'^[a-zA-Z\s]+$', author_name):
            raise serializers.ValidationError('name must contain only English letters and spaces.')

        functions.name_exists(self, author_name, Author)

        return author_name
