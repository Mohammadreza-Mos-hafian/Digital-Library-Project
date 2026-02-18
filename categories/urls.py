from django.urls import path

from .views import CategoryListCreateAPIView, CategoryDetailAPIView

app_name = 'categories'

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='categories-list-create'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
]
