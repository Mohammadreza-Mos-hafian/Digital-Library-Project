from rest_framework import serializers

from utils import functions

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']

    def validate_name(self, value: str):
        category_name = ' '.join(value.strip().split()).capitalize()

        if len(category_name) < 3:
            raise serializers.ValidationError('name must be at least 3 characters long.')

        functions.contains_english_letter(category_name, 'name')

        functions.name_exists(self, category_name, Category)

        return category_name
