from django.urls import path

from .views import CategoryListCreateView

app_name = 'categories'

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='categories-list'),
]
