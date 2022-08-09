from django.urls import re_path


from .views import Inventory

app_name = 'inventory'
STATIC_ROOT = 'Static'

urlpatterns = [
    re_path(r'^fetch_inventory', Inventory.as_view(), name="inventory"),

]