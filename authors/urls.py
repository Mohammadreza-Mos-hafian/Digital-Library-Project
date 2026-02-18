from django.urls import path

from .views import AuthorListCreateAPIView, AuthorDetailAPIView

app_name = 'authors'

urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='authors-list'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view(), name='author-detail'),
]
