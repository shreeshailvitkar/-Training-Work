from django.shortcuts import render
from rest_framework import viewsets, permissions
from cricket.models import (
    Team,
    Bowler,
    Batsman
)
from api.serializers import (
    TeamSerializer,
    BowlerSerializer,
    BatsmanSerializer
)

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permissions_classes = [permissions.IsAuthenticated]

class BowlerViewSet(viewsets.ModelViewSet):
    queryset = Bowler.objects.all()
    serializer_class = BowlerSerializer
    permissions_classes = [permissions.IsAuthenticated]

class BatsmanViewSet(viewsets.ModelViewSet):
    queryset = Batsman.objects.all()
    serializer_class = BatsmanSerializer
    permissions_classes = [permissions.IsAuthenticated]
