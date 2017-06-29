from django.contrib import admin
from django.contrib.admin.sites import AdminSite

from main.models import *

AdminSite.site_header = 'Управление умным домом'
AdminSite.site_title = 'Умный дом'


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    ordering = ['name']