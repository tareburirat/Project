from django.contrib import admin

from apps.bank_accounts.models import BankAccount


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'bank', 'account_owner', 'card_type', 'is_active', 'promptpay_phone_number',
                    'promptpay_citizen_id')
    search_fields = ('id', 'bank', 'account_owner', 'card_type', 'is_active', 'promptpay_phone_number',
                     'promptpay_citizen_id')
