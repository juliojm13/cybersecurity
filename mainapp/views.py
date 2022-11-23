from django.shortcuts import render
from django.views.generic import RedirectView, TemplateView


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


index_view = IndexView.as_view()
