from django.contrib import admin
from .models import InventoryModel, InventoryUnit, InventoryChangeModel


# Register your models here.
class InventoryModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class InventoryUnitAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class InventoryChangeModelAdmin(admin.ModelAdmin):
    list_display = ('inventory','quantity')
    search_fields = ('inventory','quantity')
    list_filter = ('inventory','quantity')


admin.site.register(InventoryModel, InventoryModelAdmin)
admin.site.register(InventoryUnit, InventoryUnitAdmin)
admin.site.register(InventoryChangeModel, InventoryChangeModelAdmin)
