from django.contrib import admin
from .models import Item, Tag, Category


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "is_published"]
    list_editable = ["is_published"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "is_published"]
    list_editable = ["is_published"]


@admin.register(Category)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ["name", "is_published"]
    list_editable = ["is_published"]
