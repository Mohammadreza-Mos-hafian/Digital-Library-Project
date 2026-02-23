from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Author
from .serializers import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all_without_deleted()
    serializer_class = AuthorSerializer

    def get_success_headers(self, data):
        try:
            return {
                'Location': reverse('author-detail', kwargs={'pk': data['id']}, request=self.request)
            }
        except (TypeError, KeyError):
            return {}


def destroy(self, request, *args, **kwargs):
    instance: Author = self.get_object()
    instance.soft_delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
