from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff')
    list_editable = ('is_staff', )
    ordering = ('email', )
    StackedInline = ('birthday', )
