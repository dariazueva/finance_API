from decimal import Decimal

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Account, Transaction


class AccountViewSetTest(APITestCase):
    def setUp(self):
        self.account = Account.objects.create(name="Test Account")
        Transaction.objects.create(account=self.account,
                                   amount=Decimal("100.00"))

    def test_list_accounts(self):
        response = self.client.get(reverse("account-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Test Account")
        self.assertEqual(response.data[0]["balance"], "100.00")


class TransactionViewSetTest(APITestCase):
    def setUp(self):
        self.account = Account.objects.create(name="Test Account")
        self.transaction = Transaction.objects.create(
            account=self.account, amount=Decimal("100.00"))

    def test_list_transactions(self):
        response = self.client.get(reverse("transaction-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["amount"], "100.00")
        self.assertEqual(response.data[0]["account_balance"], "100.00")
