from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .filters import TransactionFilter
from .models import Account, Transaction
from .serializers import (AccountDetailSerializer, AccountSerializer,
                          TransactionDetailSerializer, TransactionSerializer)


class AccountViewSet(viewsets.ModelViewSet):
    """ViewSet для управления счетами."""

    queryset = Account.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return AccountDetailSerializer
        return AccountSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """ViewSet для управления операциями."""

    queryset = Transaction.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransactionFilter

    def get_serializer_class(self):
        if self.action == "list":
            return TransactionSerializer
        return TransactionDetailSerializer
