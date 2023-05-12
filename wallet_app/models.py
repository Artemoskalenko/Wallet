from django.db import models
from django.conf import settings

import datetime


class Currency(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=3)
    convertion_rate = models.DecimalField(decimal_places=8, max_digits=20)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"


class Wallet(models.Model):
    GENERAL = "General"
    CASH = "Cash"
    CREDIT_CARD = "Credit card"
    ACCOUNT_TYPE_CHOICES = (
        (GENERAL, "General"),
        (CASH, "Cash"),
        (CREDIT_CARD, "Credit card"),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user", on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2, max_digits=30)
    color = models.CharField(max_length=10)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES, default=GENERAL)
    exclude_from_statistic = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.balance} {self.currency}"

    class Meta:
        verbose_name = "Счёт"
        verbose_name_plural = "Счета"


class BalanceHistory(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2, max_digits=30)

    def __str__(self):
        return f"{self.date_time}: {self.wallet} - {self.balance}"

    class Meta:
        verbose_name = "История счета"
        verbose_name_plural = "Истории счетов"


class Category(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Record(models.Model):
    INCOME = "IN"
    EXPENSE = "EX"
    TYPE_CHOICES = (
        (INCOME, "Income"),
        (EXPENSE, "Expense"),
    )

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=INCOME)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=30)
    note = models.TextField(max_length=150)
    date_time = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        if self.type == self.INCOME:
            return f"{self.wallet.name}: +{self.amount} {self.currency}"
        else:
            return f"{self.wallet.name}: -{self.amount} {self.currency}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
