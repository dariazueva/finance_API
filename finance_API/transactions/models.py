from django.db import models


class Account(models.Model):
    name = models.CharField('Название счета',
                            max_length=100)

    class Meta:
        verbose_name = 'Счёт'
        verbose_name_plural = 'Счета'
        ordering = ('name',)

    def __str__(self):
        return self.name

    @property
    def balance(self):
        transactions = Transaction.objects.filter(account_id=self.id)
        return sum(transaction.amount for transaction in transactions)


class Transaction(models.Model):
    account_id = models.ForeignKey(Account,
                                   on_delete=models.CASCADE,
                                   verbose_name='Идентификатор счета')
    date = models.DateField('Дата создания транзакции',
                            auto_now_add=True)
    amount = models.DecimalField('Сумма операции',
                                 max_digits=10,
                                 decimal_places=2)

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'

    def __str__(self):
        return f"Transaction of {self.account_id.name} on {self.date}"
