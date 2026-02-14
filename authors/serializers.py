import re

from rest_framework import serializers

from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']
        read_only_fields = ['id']

    def validate_name(self, value: str):
        if len(value) < 3:
            raise serializers.ValidationError('Author name must be at least 3 characters long.')

        if not re.match(r'^[a-zA-Z\s]+$', value):
            raise serializers.ValidationError('Name must contain only English letters and spaces.')

        return value.capitalize()
