from django.urls import re_path


from .views import InventoryUnitsView, InventoryView, InventorysView

app_name = 'inventory'
STATIC_ROOT = 'Static'

urlpatterns = [
    re_path(r'^fetch_inventory', InventorysView.as_view(), name="inventorys"),
    re_path(r'^inventory', InventoryView.as_view(), name="inventory"),
    re_path(r'^units', InventoryUnitsView.as_view(), name="units"),

]