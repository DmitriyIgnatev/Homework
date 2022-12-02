from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'first_name',
        'second_name',
        'birthday',
        'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'second_name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
    fieldsets = (
        (None, {
            'fields': ('email', 'password')}),
        ('Персональная информация', {
            'fields': ('first_name', 'second_name', 'birthday')}),
        ('Статус', {
            'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Остальные штуки', {'fields': ('last_login',)}),
    )
