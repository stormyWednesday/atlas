from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'base/_base.html'
    # template_name = 'index.html'
