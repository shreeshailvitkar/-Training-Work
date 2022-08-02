from django.urls import path

from entries.views import HomeView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
]
