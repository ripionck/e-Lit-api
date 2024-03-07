from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, UserModelSerializer
from .models import CustomUser

# Create your views here.
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserProfileCreateView(generics.ListCreateAPIView):
    """Generic View for listing and Creating User Profiles"""

    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [AllowAny]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
