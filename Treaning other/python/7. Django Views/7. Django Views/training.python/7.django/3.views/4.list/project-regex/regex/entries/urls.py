from django.urls import path

from entries.views import (
    HomeView,
    ListView,
)

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('list/', ListView.as_view(), name='list'),
]
