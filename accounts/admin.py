from django.contrib import admin
from django.contrib.admin.forms import AdminAuthenticationForm

from accounts.models import User, PhoneToken


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'phone_number', 'username')
    search_fields = ('phone_number',)
    list_filter = ('phone_number',)
    readonly_fields = ('phone_number', 'username',)


class PhoneTokenAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)
    search_fields = ('phone_number',)
    list_filter = ('phone_number',)


admin.site.register(User, UserAdmin)

admin.site.register(PhoneToken, PhoneTokenAdmin)
