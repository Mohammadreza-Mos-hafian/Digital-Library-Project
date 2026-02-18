from django.shortcuts import reverse
from rest_framework.generics import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Author
from .serializers import AuthorSerializer


class AuthorListCreateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        authors = Author.objects.all_without_deleted()
        serializer = AuthorSerializer(authors, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        serializer = AuthorSerializer(data=request.data)

        if serializer.is_valid():
            instance = serializer.save()

            url = reverse('authors:author-detail', kwargs={'pk': instance.pk})
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers={
                    'Location': request.build_absolute_uri(url)
                }
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailAPIView(APIView):
    def get_object(self):
        return get_object_or_404(
            queryset=Author.objects.all_without_deleted(),
            pk=self.kwargs['pk']
        )

    def get(self, request, *args, **kwargs):
        author = self.get_object()
        serializer = AuthorSerializer(author)
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )

    def put(self, request, *args, **kwargs):
        author = self.get_object()
        serializer = AuthorSerializer(author, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        author = self.get_object()
        serializer = AuthorSerializer(author, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        author = self.get_object()
        author.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
