from django.contrib import admin

# Register your models here.
from apps.transactions.models import Transaction


@admin.register(Transaction)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'object_trans', 'date_action', 'action']
    search_fields = ['id']