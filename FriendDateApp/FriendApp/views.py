from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status



# Create your views here.


def index(request):
    return render(request, 'FriendApp/index.html')

#def create(request):
    # if request.method == 'POST':
        # first_name = request.POST.get('first_name')
        # last_name = request.Post.get('last_name')



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
        serializer = UserSerializer(user)
        comment.delete()
        return Response(serializer.data)    



