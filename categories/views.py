from django.shortcuts import reverse
from rest_framework.generics import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category
from .serializers import CategorySerializer


class CategoryListCreateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all_without_deleted()
        serializer = CategorySerializer(categories, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            instance = serializer.save()

            url = reverse('categories:category-detail', kwargs={'pk': instance.pk})
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers={
                    'Location': request.build_absolute_uri(url)
                }
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):
    def get_object(self):
        return get_object_or_404(
            queryset=Category.objects.all_without_deleted(),
            pk=self.kwargs['pk']
        )

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = CategorySerializer(category)
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )

    def put(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = CategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = CategorySerializer(category, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        category = self.get_object()
        category.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
