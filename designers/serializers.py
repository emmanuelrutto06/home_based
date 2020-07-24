from rest_framework import serializers
from .models import Registration


class RegistrationSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    Email = serializers.EmailField()
    password = serializers.CharField()
    phonenumber = serializers.CharField(max_length=50)


    class Meta:
        model=Registration
        fields ='__all__'