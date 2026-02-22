from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all_without_deleted()
    serializer_class = CategorySerializer

    def destroy(self, request, *args, **kwargs):
        instance: Category = self.get_object()
        instance.soft_delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
