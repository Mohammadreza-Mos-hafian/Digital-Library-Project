from django.urls import reverse
from rest_framework.generics import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Book
from .serializers import BookSerializer


class BookListCreateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all_without_deleted()
        serializer = BookSerializer(books, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            instance = serializer.save()

            url = reverse('books:book-detail', kwargs={'pk': instance.pk})
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers={
                    'Location': request.build_absolute_uri(url)
                }
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailAPIView(APIView):
    def get_object(self):
        return get_object_or_404(
            queryset=Book.objects.all_without_deleted(),
            pk=self.kwargs['pk']
        )

    def get(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = BookSerializer(book, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        book.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
