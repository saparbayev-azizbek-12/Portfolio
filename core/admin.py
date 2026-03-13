"""
Admin configuration for the core app.
"""

from django.contrib import admin
from .models import Experience, Project, ContactMessage


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'start_date', 'end_date', 'order')
    list_editable = ('order',)
    search_fields = ('company', 'role')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'featured', 'order', 'created')
    list_filter = ('level', 'featured')
    list_editable = ('featured', 'order')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_read', 'created')
    list_filter = ('is_read', 'created')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'created')
    list_editable = ('is_read',)
