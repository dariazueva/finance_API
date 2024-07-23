from rest_framework import serializers

from .models import Account, Transaction


class AccountSerializer(serializers.ModelSerializer):
    """Сериализатор для создания счёта."""

    class Meta:
        model = Account
        fields = ["id", "name"]


class AccountDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода списка счетов."""

    balance = serializers.DecimalField(max_digits=10,
                                       decimal_places=2,
                                       read_only=True)

    class Meta:
        model = Account
        fields = ["id", "name", "balance"]


class TransactionDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для создания операции."""

    class Meta:
        model = Transaction
        fields = ["id", "account", "date", "amount"]


class TransactionSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода списка операций."""

    account_balance = serializers.DecimalField(max_digits=10,
                                               decimal_places=2,
                                               read_only=True)

    class Meta:
        model = Transaction
        fields = ["id", "account", "account_balance", "date", "amount"]
        read_only_fields = ["account_balance"]
