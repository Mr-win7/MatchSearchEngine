# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from apiv1.models import *

# Register your models here.

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'url', 'time')
