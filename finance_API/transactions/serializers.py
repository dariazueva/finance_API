from rest_framework import serializers

from .models import Account, Transaction


class AccountSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(max_digits=10,
                                       decimal_places=2,
                                       read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'name', 'balance']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'account_id', 'date', 'amount']
