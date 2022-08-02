from django.urls import path

from entries.views import (
    DetailView,
    HomeView,
    ListView,
)

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('list/', ListView.as_view(), name='list'),
    path('<int:pk>/detail/', DetailView.as_view(), name='detail'),
]
