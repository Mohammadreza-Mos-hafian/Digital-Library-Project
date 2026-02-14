from django.urls import path

from .views import AuthorListCreateView

app_name = 'authors'

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='authors-list'),
]
