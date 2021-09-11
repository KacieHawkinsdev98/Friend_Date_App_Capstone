from django.urls.resolvers import URLPattern
from . import views
from django.urls import path 

app_name = 'FriendApp'
urlpatterns = [
    path('', views.index, name='index')
]

