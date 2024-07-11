from rest_framework import generics
from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer

class AccountListCreate(generics.ListCreateAPIView):
    queryset = Account.objects.all().order_by('id')
    serializer_class = AccountSerializer

class TransactionListCreate(generics.ListCreateAPIView):
    queryset = Transaction.objects.all().order_by('-date')
    serializer_class = TransactionSerializer

class TransactionDelete(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_url_kwarg = 'id'

class TransactionFilteredList(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all().order_by('-date')

        accounts = self.request.query_params.getlist('accounts')
        if accounts:
            queryset = queryset.filter(account_id__in=accounts)

        date_from = self.request.query_params.get('date_from')
        if date_from:
            queryset = queryset.filter(date__gte=date_from)

        date_to = self.request.query_params.get('date_to')
        if date_to:
            queryset = queryset.filter(date__lte=date_to)

        amount_from = self.request.query_params.get('amount_from')
        if amount_from:
            queryset = queryset.filter(amount__gte=amount_from)

        amount_to = self.request.query_params.get('amount_to')
        if amount_to:
            queryset = queryset.filter(amount__lte=amount_to)

        return queryset
