from django.contrib import admin

# Register your models here.
from apps.accounts.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'first_name', 'last_name', 'email', 'phone', 'coin']
    search_fields = ['display_name', 'username', 'first_name', 'last_name', 'email']
