# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from organization.models import Organization
# Register your models here.

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(Organization, OrganizationAdmin)
