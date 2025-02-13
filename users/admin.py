from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'number', 'birth_date', 'created_at', 'updated_at')
    list_filter = ('id', 'login', 'number', 'birth_date')
    search_fields = ('id', 'login', 'number', 'birth_date')
