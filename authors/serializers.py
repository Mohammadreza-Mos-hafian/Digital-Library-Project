from rest_framework import serializers

from utils import functions

from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']
        read_only_fields = ['id']

    def validate_name(self, value: str):
        author_name = ' '.join(value.strip().split()).title()

        if len(author_name) < 3:
            raise serializers.ValidationError('name must be at least 3 characters long.')

        functions.contains_english_letter(author_name, 'name')

        functions.is_exist(self, 'name', author_name, Author)

        return author_name
