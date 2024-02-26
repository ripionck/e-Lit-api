from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet

router = DefaultRouter()
router.register('review', ReviewViewSet, basename='book-reviews')

"""
POST /review/ - Create a new publisher
GET  /review/?book_id={book_id} - Retrieve a review by book ID
"""
urlpatterns = [
    path('', include(router.urls)),
]

