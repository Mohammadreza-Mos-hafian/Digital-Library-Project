from rest_framework import serializers

from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']
        read_only_fields = ['id']

    def validate_name(self, value: str):
        if len(value) < 3:
            raise serializers.ValidationError('The author name must be at least 3 characters long.')
        return value
