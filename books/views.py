from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all_without_deleted()
    serializer_class = BookSerializer

    def get_success_headers(self, data):
        try:
            return {
                'Location': reverse('book-detail', kwargs={'pk': data['id']}, request=self.request)
            }
        except (TypeError, KeyError):
            return {}

    def destroy(self, request, *args, **kwargs):
        instance: Book = self.get_object()
        instance.soft_delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
