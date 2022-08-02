from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = '/admin/login/'
    template_name = 'entries/home.html'

    def get(self, request, *args, **kwargs):
        context = {'username': request.user}
        return self.render_to_response(context)
