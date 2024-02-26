from django.urls import path, include
from rest_framework import routers
from .views import PublisherViewSet


router = routers.DefaultRouter()
router.register('publisher', PublisherViewSet, basename='publisher')

"""
GET /publisher/ - List all publishers
POST /publisher/ - Create a new publisher
GET /publisher/{pk}/ - Retrieve an publisher by ID
PUT /publisher/{pk}/ - Update an publisher by ID
PATCH /publisher/{pk}/ - Partially update an publisher by ID
DELETE /publisher/{pk}/ - Delete a publisher by ID

"""


urlpatterns = [
  path('', include(router.urls))
]

