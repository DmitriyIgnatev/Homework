from django.contrib import admin
from .models import Catalog_item, Catalog_tag, Catalog_category


admin.register(Catalog_item)
admin.register(Catalog_tag)
admin.register(Catalog_category)
