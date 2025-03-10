from django.shortcuts import render
from blogapp.serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["POST"])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)    #the data=request.data portion seems to be passing in the fields that the UserRegistrationSerializer has (username, first_name, last_name, etc.)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)