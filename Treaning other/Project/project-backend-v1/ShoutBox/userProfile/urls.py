import imp
from unicodedata import name
from django.urls import URLPattern, path
from userProfile.views import RegisterView



urlpatterns = [
    path('register/', RegisterView.as_view(), name='register')
]