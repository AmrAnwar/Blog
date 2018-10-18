# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post


# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'type']
    list_display_links = ['timestamp']
    list_editable = ['title']
    list_filter = ['user', 'timestamp']


admin.site.register(Post, admin_class=PostModelAdmin)
