from django.urls import (
    include,
    path,
)
from rest_framework import routers

from api.views import EntryViewSet

router = routers.DefaultRouter()
router.register(r'entries', EntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
