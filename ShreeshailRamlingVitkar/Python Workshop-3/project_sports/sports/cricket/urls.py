from django.urls import path
from cricket.views import ( 
    HomePage,
    TeamView,
    BatsmanView,
    BowlerView
 )

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('team/', TeamView.as_view(), name = 'team'),
    path('bowler/', BowlerView.as_view(), name = 'bowler'),
    path('batsman/', BatsmanView.as_view(), name = 'batsman'),
   
]

