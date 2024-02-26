from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet


router = routers.DefaultRouter()
router.register('book', BookViewSet, basename='book')

"""
GET /book/ - List all books
POST /book/ - Create a new book
GET /book/{pk}/ - Retrieve an book by ID
PUT /book/{pk}/ - Update an book by ID
PATCH /book/{pk}/ - Partially update an book by ID
DELETE /book/{pk}/ - Delete an book by ID

"""


urlpatterns = [
  path('', include(router.urls))
]

