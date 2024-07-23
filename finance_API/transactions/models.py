from django.db import models


class Account(models.Model):
    """Модель 'Счёт'."""

    name = models.CharField("Название счета",
                            max_length=100)

    class Meta:
        verbose_name = "Счёт"
        verbose_name_plural = "Счета"
        ordering = ("id",)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    """Модель 'Операция'."""

    account = models.ForeignKey(Account,
                                on_delete=models.CASCADE,
                                verbose_name="Идентификатор счета",
                                related_name="transactions")
    date = models.DateField("Дата создания транзакции",
                            auto_now_add=True)
    amount = models.DecimalField("Сумма операции",
                                 max_digits=10,
                                 decimal_places=2)

    class Meta:
        verbose_name = "Операция"
        verbose_name_plural = "Операции"
        ordering = ("-date",)

    def __str__(self):
        return f"Transaction of {self.account.name} on {self.date}"
