from django.urls import path

from .views import BookDetailAPIView, BookListCreateAPIView

app_name = 'books'

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='books-list-create'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='books-details')
]
