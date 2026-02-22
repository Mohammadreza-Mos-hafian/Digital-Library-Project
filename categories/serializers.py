from rest_framework import serializers

from utils import functions

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='category-detail')

    class Meta:
        model = Category
        fields = ['id', 'url', 'name']
        read_only_fields = ['id']

    def validate_name(self, value: str):
        category_name = ' '.join(value.strip().split()).title()

        if len(category_name) < 3:
            raise serializers.ValidationError('name must be at least 3 characters long.')

        functions.contains_english_letter(category_name, 'name')

        functions.is_exist(self, 'name', category_name, Category)

        return category_name
