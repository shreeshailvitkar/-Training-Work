from dataclasses import fields
from statistics import mode
from rest_framework import serializers

from appusers.models import Profile, FriendRequest
from django.contrib.auth.models import User



class UserModleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password'
        ]


class UsersProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        
        fields = [
            'user',
            'bio',
            'friends',
           
        ]