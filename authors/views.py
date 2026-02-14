from rest_framework import generics

from .models import Author
from .serializers import AuthorSerializer


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all_without_deleted()
    serializer_class = AuthorSerializer
