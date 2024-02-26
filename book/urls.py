from django.urls import path, include
from rest_framework import routers
from .views import AuthorViewSet


router = routers.DefaultRouter()
router.register('author', AuthorViewSet, basename='author')

"""
GET /author/ - List all authors
POST /author/ - Create a new author
GET /author/{pk}/ - Retrieve an author by ID
PUT /author/{pk}/ - Update an author by ID
PATCH /author/{pk}/ - Partially update an author by ID
DELETE /author/{pk}/ - Delete an author by ID

"""


urlpatterns = [
  path('', include(router.urls))
]

