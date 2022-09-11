from django.urls import re_path


from .views import OrganizationView

app_name = 'organization'
STATIC_ROOT = 'Static'

urlpatterns = [
    re_path(r'^organization', OrganizationView.as_view(), name="inventorys"),
]