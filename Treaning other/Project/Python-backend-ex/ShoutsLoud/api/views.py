from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from api.serializers import EntrySerializer
from entries.models import UserData


# Create your views here.
class EntryViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]