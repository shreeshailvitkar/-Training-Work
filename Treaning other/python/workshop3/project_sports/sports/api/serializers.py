from django.contrib.auth.models import User
from rest_framework import serializers
from cricket.models import (
    Team,
    Bowler,
    Batsman
)


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            'id',
            'owner',
            'team_name'
        ]

class BowlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bowler
        fields = [
            'name',

        ]

class BatsmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batsman
        fields = [
            'name',
            
        ]