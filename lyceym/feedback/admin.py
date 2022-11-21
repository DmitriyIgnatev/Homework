from django.contrib import admin
from .models import FeedbackModel


@admin.register(FeedbackModel)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_on',)
