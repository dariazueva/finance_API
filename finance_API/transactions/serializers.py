from rest_framework import serializers
from django.db.models import Sum, Q, Window
from django.db.models.functions import Coalesce

from .models import Account, Transaction


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'name']


class AccountDetailSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(max_digits=10,
                                       decimal_places=2,
                                       read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'name', 'balance']


class TransactionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['id', 'account', 'date', 'amount']


class TransactionSerializer(serializers.ModelSerializer):
    account_balance = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'account', 'account_balance', 'date', 'amount']
        read_only_fields = ['account_balance']

    def get_account_balance(self, obj):
        transactions = Transaction.objects.filter(
            account=obj.account,
            date__lt=obj.date
        ).order_by('date', 'id')
        balance = transactions.aggregate(balance=Coalesce(Sum('amount'), 0))['balance']
        return balance
