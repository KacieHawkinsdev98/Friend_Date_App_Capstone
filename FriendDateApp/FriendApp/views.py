from django.contrib.auth.models import User
from .serializers import RegistrationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


def index(request):
    return render(request, 'FriendApp/index.html')


class UserList(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    
    def get_object(self, pk):
        try:
          return User.objects.get(pk=pk)
        except User.DoesNotExist:
           raise Http404     

    def get(self, request, pk):
        users = self.get_object(pk)
        serializer = UserSerializer()
        return Response(serializer.data)

    def delete(self, request, pk):
        users = self.get_object(pk)
        serializer = UserSerializer(users)
        users.delete()
        return Response(serializer.data)    



