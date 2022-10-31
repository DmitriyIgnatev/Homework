from django.contrib import admin
from .models import Catalog_item, Catalog_tag, Catalog_category


admin.site.register(Catalog_item)
admin.site.register(Catalog_tag)
admin.site.register(Catalog_category)
