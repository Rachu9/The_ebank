from django.contrib import admin
from .models import Account, Transaction, BillPayment

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    search_fields = ('user__username',)
    list_filter = ('user',)
    readonly_fields = ('user',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'amount', 'timestamp')
    search_fields = ('sender__user__username', 'receiver__user__username')
    list_filter = ('timestamp',)
    readonly_fields = ('timestamp',)


@admin.register(BillPayment)
class BillPaymentAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'bill_type', 'timestamp')
    search_fields = ('account__user__username', 'bill_type')
    list_filter = ('timestamp', 'bill_type')
    readonly_fields = ('timestamp',)
