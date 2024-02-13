from .models import EMmodel, Loginuser
from rest_framework import serializers

class EMSerializer(serializers.ModelSerializer):
    class Meta:
        model = EMmodel
        fields = ('__all__')


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loginuser
        fields = ('username','password')