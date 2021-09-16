from .import views
from django.urls import path 
from .serializers import User 


urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),

]


