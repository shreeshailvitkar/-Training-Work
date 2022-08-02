from multiprocessing import context
from re import template
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from cricket.models import Team, Batsman, Bowler


# Create your views here.

class HomePage(TemplateView):
    template_name = 'index.html'


class TeamView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'entries_team'
    template_name = 'team.html'
    def get_queryset(self):
        return Team.objects.all()

class TeamView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'entries_team'
    template_name = 'team.html'
    def get_queryset(self):
        return Team.objects.all()

class BatsmanView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'entries_team'
    template_name = 'batsman.html'
    def get_queryset(self):
        return Batsman.objects.all()

class BowlerView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'entries_team'
    template_name = 'bowler.html'
    def get_queryset(self):
        return Bowler.objects.all()

