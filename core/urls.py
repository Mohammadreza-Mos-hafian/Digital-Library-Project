from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authors.views import AuthorViewSet
from categories.views import CategoryViewSet
from books.views import BookViewSet
from core.views import home_page

router = DefaultRouter()

router.register('authors', AuthorViewSet, basename='author')
router.register('categories', CategoryViewSet, basename='category')
router.register('books', BookViewSet, basename='book')

urlpatterns = [
    path('', home_page),
    path('api/', include(router.urls))
]
