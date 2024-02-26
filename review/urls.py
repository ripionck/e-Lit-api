from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet

router = DefaultRouter()
router.register('review', ReviewViewSet, basename='book-reviews')

"""
/review/ - (GET, POST)
/review/?book_id=1 - (GET, PUT, PATCH, DELETE)
"""
urlpatterns = [
    path('', include(router.urls)),
]

