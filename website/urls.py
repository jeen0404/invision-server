from django.urls import re_path
from django.views.generic import TemplateView

app_name = 'website'
STATIC_ROOT = 'Static'

urlpatterns = [
    re_path('^$', TemplateView.as_view(template_name='index.html')),
]