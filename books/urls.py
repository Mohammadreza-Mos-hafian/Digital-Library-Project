from django.urls import path

from .views import BookListCreateView

app_name = 'books'

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='books-list-create'),
]
