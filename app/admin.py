from django.contrib import admin
from .models import React, Posting

class ReactAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password']

class PostingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'problem']

admin.site.register(React, ReactAdmin)
admin.site.register(Posting, PostingAdmin)
