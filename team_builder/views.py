from django.http import HttpResponse
from django.views.generic import View, TemplateView


class Home(TemplateView):
    template_name = 'index.html'