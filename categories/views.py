from rest_framework import generics

from .models import Category
from .serializers import CategorySerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all_without_deleted()
    serializer_class = CategorySerializer
