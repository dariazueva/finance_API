from rest_framework import viewsets, generics

from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all().order_by('id')
    serializer_class = AccountSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('-date')
    serializer_class = TransactionSerializer


class TransactionDeleteView(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_url_kwarg = 'id'


class TransactionFilteredListView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all().order_by('-date')

        params = {
            'accounts': self.request.query_params.getlist('accounts'),
            'date_from': self.request.query_params.get('date_from'),
            'date_to': self.request.query_params.get('date_to'),
            'amount_from': self.request.query_params.get('amount_from'),
            'amount_to': self.request.query_params.get('amount_to'),
        }

        filters = {}
        if params['accounts']:
            filters['account_id__in'] = params['accounts']
        if params['date_from']:
            filters['date__gte'] = params['date_from']
        if params['date_to']:
            filters['date__lte'] = params['date_to']
        if params['amount_from']:
            filters['amount__gt'] = params['amount_from']
        if params['amount_to']:
            filters['amount__lte'] = params['amount_to']

        if filters:
            queryset = queryset.filter(**filters)

        return queryset
