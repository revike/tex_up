from django.core.validators import RegexValidator
from django.db import models


class Client(models.Model):
    """Таблица клиенты"""
    first_name = models.CharField(max_length=128, blank=False,
                                  verbose_name='имя')
    phone_number_regex = RegexValidator(regex=r"^\+1?\d{11,11}$")
    phone = models.CharField(validators=[phone_number_regex], max_length=16,
                             unique=True, blank=False, verbose_name='телефон')

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "client"
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
