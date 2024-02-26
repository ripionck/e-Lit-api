from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet


router = routers.DefaultRouter()
router.register('book', BookViewSet, basename='book')

"""
GET /book/ - List all books
POST /book/ - Create a new book
GET /book/{pk}/ - Retrieve a book by ID
PUT /book/{pk}/ - Update a book by ID
PATCH /book/{pk}/ - Partially update a book by ID
DELETE /book/{pk}/ - Delete a book by ID

"""


urlpatterns = [
  path('', include(router.urls))
]

