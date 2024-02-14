from .models import EMmodel
from rest_framework import serializers
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class EMSerializer(serializers.ModelSerializer):
    class Meta:
        model = EMmodel
        fields = ('__all__')


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = EMmodel
        fields = ('name','username','email','department','address')
        
        
'''class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
        return token'''
    