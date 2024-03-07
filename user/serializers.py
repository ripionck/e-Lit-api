from rest_framework import serializers, exceptions
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):
        credentials = {
            'email': attrs.get('email'),
            'password': attrs.get('password')
        }

        user = authenticate(**credentials)
        
        if user:
            if not user.is_active:
                raise exceptions.AuthenticationFailed('User is deactivated.')
            data = {}
            refresh = self.get_token(user)

            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)
            
            return data
        
        else:
            raise exceptions.AuthenticationFailed('No active account found with the given credentials.')
    
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'avatar', 'phone', 'balance']
        extra_kwargs = {'password':{'write_only':True, 'min_length': 6}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


    def to_representation(self, instance):
        """Overriding to remove password field when returning data"""
        user_data = super().to_representation(instance)
        user_data.pop('password', None)
        return user_data