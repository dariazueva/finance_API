from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (AccountViewSet, TransactionViewSet,
                    TransactionDeleteView, TransactionFilteredListView)

router = DefaultRouter()
router.register(r'accounts', AccountViewSet, basename='account')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    path('', include(router.urls)),
    path('transactions/<int:id>/', TransactionDeleteView.as_view(), name='transaction-delete'),
    path('transactions/filter/', TransactionFilteredListView.as_view(), name='transaction-filtered-list'),
]
