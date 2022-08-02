from django.views.generic import TemplateView


class HomeView(TemplateView):
    # Indicate which template needs to be used.
    template_name = 'entries/home.html'
