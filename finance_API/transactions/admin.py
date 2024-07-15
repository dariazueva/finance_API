from django.contrib import admin

from .models import Account, Transaction

admin.site.empty_value_display = 'Не задано'


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Администратор для модели Account."""

    list_display = ('name', 'balance')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """Администратор для модели Transaction."""

    list_display = ('account_id', 'date', 'amount')
    list_editable = ('amount',)
