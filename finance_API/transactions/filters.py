import django_filters

from .models import Transaction


class TransactionFilter(django_filters.FilterSet):
    """Настройка фильтра для вывода списка операций."""

    date_from = django_filters.DateFilter(field_name="date", lookup_expr='gte')
    date_to = django_filters.DateFilter(field_name="date", lookup_expr='lte')
    amount_from = django_filters.NumberFilter(field_name="amount",
                                              lookup_expr='gte')
    amount_to = django_filters.NumberFilter(field_name="amount",
                                            lookup_expr='lte')
    accounts = django_filters.BaseInFilter(field_name="account__id",
                                           lookup_expr='in')

    class Meta:
        model = Transaction
        fields = ['date_from',
                  'date_to',
                  'amount_from',
                  'amount_to',
                  'accounts']
