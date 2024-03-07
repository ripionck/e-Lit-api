from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # custom claims
        token['username']=user.username
        return token

# class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(required=True, validators = [UniqueValidator(queryset=User.objects.all())])
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = User
#         fields = ('username','first_name', 'last_name', 'email', 'password', 'password2')
#         extra_kwargs={
#             'first_name': {'required': True},
#             'last_name': {'required': True}
#         }

#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"password":"Password fields didn't match."})
        
#         return attrs
    
#     def create(self, validated_data):
#         user = User.objects.create(
#             username = validated_data['username'],
#             email = validated_data['email'],
#             first_name = validated_data['first_name'],
#             last_name = validated_data['last_name']
#         )
#         user.set_password(validated_data['password'])
#         user.save()

#         return user
    
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