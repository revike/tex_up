from django.urls import path
from django.views.generic import TemplateView

from main_app import views as main_app

app_name = 'main_app'

urlpatterns = [
    path('', main_app.IndexView.as_view(), name='index'),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt",
                                            content_type="text/plain")),
]
