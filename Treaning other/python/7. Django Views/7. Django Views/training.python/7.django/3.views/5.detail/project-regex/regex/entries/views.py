from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from entries.models import Entry


class HomeView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/admin/login/'
    template_name = 'entries/home.html'

    def get(self, request, *args, **kwargs):
        context = {'username': request.user}
        return self.render_to_response(context)


class ListView(LoginRequiredMixin, generic.ListView):
    # Defaults to entry_list if not specified.
    # That is - <model_name>_list.
    context_object_name = 'entries_list'
    # Defaults to entries/entry_list.html if not specified.
    # That is - '<app_name>/<model_name>_list.html.
    template_name = 'entries/list.html'

    # Determines the data set.
    def get_queryset(self):
        return Entry.objects.all().order_by('-date_added')


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Entry
    # Defaults to entries/entry_detail.html if not specified.
    # That is - '<app_name>/<model_name>_detail.html.
    template_name = 'entries/detail.html'
