from django.urls import (
    include,
    path,
)
from rest_framework import routers

from api.views import EntryViewSet

entry_list = EntryViewSet.as_view({
    'get': 'list',
    # Don't want this.
    # 'post': 'create',
})
entry_detail = EntryViewSet.as_view({
    'get': 'retrieve',
    # Don't want this.
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('entries/', entry_list, name='entry-list'),
    path('entries/<int:pk>/', entry_detail, name='entry-detail'),
]
