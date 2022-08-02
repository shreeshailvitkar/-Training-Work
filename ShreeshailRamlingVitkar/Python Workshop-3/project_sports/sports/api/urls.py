from unicodedata import name
from django.urls import (
    include,
    path,
)
from rest_framework import routers
from api.views import ( 
    TeamViewSet,
    BowlerViewSet,
    BatsmanViewSet 
    )
entry_list = TeamViewSet.as_view({
    'get': 'list',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
    'post': 'create',
})
entry_detail = TeamViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
    'post': 'create',
})

bowler_details = BowlerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
    'post': 'create',
})

batsman_details = BatsmanViewSet.as_view({
    #'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
    'post': 'create',
})
urlpatterns = [
    path('teams/', entry_list, name='teams-list'),
    path('teams/<int:pk>/', entry_detail, name='team-detail'),
    path('bowler/', bowler_details, name='bowler'),
    path('batsman/', batsman_details, name='batsman'),
    
]