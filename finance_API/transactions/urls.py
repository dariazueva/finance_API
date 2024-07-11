from django.urls import path
from .views import AccountListCreate, TransactionListCreate, TransactionDelete, TransactionFilteredList

urlpatterns = [
    path("accounts/", AccountListCreate.as_view(), name="account-list-create"),
    path("transactions/", TransactionListCreate.as_view(), name="transaction-list-create"),
    path("transactions/<int:id>/", TransactionDelete.as_view(), name="transaction-delete"),
    path("transactions/filter/", TransactionFilteredList.as_view(), name="transaction-filtered-list"),
]
