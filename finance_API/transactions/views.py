from decimal import Decimal

from django.db.models import DecimalField, F, Q, Sum
from django.db.models.functions import Coalesce
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .filters import TransactionFilter
from .models import Account, Transaction
from .serializers import (AccountDetailSerializer, AccountSerializer,
                          TransactionDetailSerializer, TransactionSerializer)


class AccountViewSet(viewsets.ModelViewSet):
    """ViewSet для управления счетами."""

    queryset = Account.objects.annotate(
        balance=Coalesce(Sum('transactions__amount',
                             output_field=DecimalField()), Decimal('0.0'))
    )

    def get_serializer_class(self):
        if self.action == "list":
            return AccountDetailSerializer
        return AccountSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """ViewSet для управления операциями."""

    queryset = Transaction.objects.annotate(
        account_balance=Coalesce(
            Sum('account__transactions__amount',
                filter=Q(account__transactions__date__lte=F('date')),
                output_field=DecimalField()), Decimal('0.0'))
    )
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransactionFilter

    def get_serializer_class(self):
        if self.action == "list":
            return TransactionSerializer
        return TransactionDetailSerializer
