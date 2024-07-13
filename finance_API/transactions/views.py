from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status

from .models import Account, Transaction
from .serializers import (AccountDetailSerializer, AccountSerializer,
                          TransactionSerializer, TransactionDetailSerializer)
from .filters import TransactionFilter


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AccountDetailSerializer
        return AccountSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransactionFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return TransactionSerializer
        return TransactionDetailSerializer

