import re

from rest_framework import serializers

from .models import Category

from utils import functions


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']

    def validate_name(self, value: str):
        category_name = ' '.join(value.strip().split()).capitalize()

        if len(category_name) < 3:
            raise serializers.ValidationError('category name must be at least 3 characters long.')

        if not re.match(r'^[a-zA-Z\s]+$', category_name):
            raise serializers.ValidationError('name must contain only English letters and spaces.')

        functions.name_exists(self, 'category', category_name, Category)

        return category_name
