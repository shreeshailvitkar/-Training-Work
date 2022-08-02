from django.urls import (
    include,
    path,
)
from rest_framework import routers
from appusersAPI.views import UsersProfiles, UserModelsData



router = routers.DefaultRouter()
router.register(r'usersProfile', UsersProfiles)
router.register(r'userLogin', UserModelsData)

urlpatterns = [
    path('', include(router.urls)),
]
