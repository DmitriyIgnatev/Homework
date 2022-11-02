from django.contrib import admin
from .models import Item, Tag, Category


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_published']
    list_editable = ['is_published']
    filter_horizontal = ['tag']
    list_display_links = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_published']
    list_editable = ['is_published']
    list_display_links = ['name']


@admin.register(Category)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_published']
    list_editable = ['is_published']
    list_display_links = ['name']
