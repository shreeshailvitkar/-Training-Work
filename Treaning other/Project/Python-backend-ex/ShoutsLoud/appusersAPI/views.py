from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from appusersAPI.serializers import UserModleSerializer

from appusersAPI.serializers import UsersProfileSerializer
from appusers.models import Profile, FriendRequest
from django.contrib.auth.models import User


# Create your views here.

class UsersProfiles(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UsersProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserModelsData(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModleSerializer
    permission_classes = [permissions.IsAuthenticated]
