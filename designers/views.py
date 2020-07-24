from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from . models import Registration
from . serializers import RegistrationSerializer

class clientList(APIView):

    def get(self, request):
        model = Registration.objects.all()
        serializer=RegistrationSerializer(model, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializers=RegistrationSerializer(data=request.data)
        if (serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class clientDetails(APIView):
        def get_clients_list(self, Email):
            try:
                model = Registration.objects.get(Email=Email)
                return model
            except Registration.DoesNotExist:
                return

        def get(self, request, Email):
            if not self.get_clients_list(Email):
                return Response(f'client with Email {Email} is Not Found in the database', status=status.HTTP_404_NOT_FOUND)
            serializer = RegistrationSerializer(self.get_clients_list(Email))
            return Response(serializer.data)

        def put(self, request, Email):
            serializers=RegistrationSerializer(self.get_clients_list(Email), data=request.data)
            if (serializers.is_valid()):
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, Email):
            if not self.get_clients_list(Email):
                return Response(f'client with Email {Email} is erased from the database', status=status.HTTP_204_NO_CONTENT)
            model = self.get_clients_list(Email)
            model.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)