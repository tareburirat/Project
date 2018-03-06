from django.contrib import admin

from apps.coin_transactions.models import CoinTransaction


@admin.register(CoinTransaction)
class CoinTransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'account', 'get_transaction_type_display', 'amount', 'promoted_product']
    search_fields = ['id', 'account__display_name', 'promoted_product__name']
