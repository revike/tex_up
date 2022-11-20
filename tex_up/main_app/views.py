from django.urls import reverse_lazy
from django.views.generic import CreateView

from main_app.forms import ClientForm
from main_app.models import Client
from main_app.utils import send_mail_client


class IndexView(CreateView):
    """Контроллер главной страницы"""
    template_name = 'main_app/index.html'
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main_app:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'tex-UP'
        return context

    def form_valid(self, form):
        send_mail_client(form.cleaned_data)
        return super().form_valid(form)
