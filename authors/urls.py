from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet

app_name = 'authors'

router = DefaultRouter()

router.register('authors', AuthorViewSet, basename='author')

urlpatterns = router.urls
