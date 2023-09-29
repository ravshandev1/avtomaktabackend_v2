from django.db import models
from client.models import Category
from instructor.models import Instructor


class Car(models.Model):
    class Meta:
        verbose_name_plural = 'Мошиналар'
        verbose_name = 'Мошиналар'

    nomi = models.CharField(max_length=255)
    categoriyasi = models.ForeignKey(Category, models.CASCADE)

    def __str__(self):
        return f"{self.nomi} {self.categoriyasi.toifa}"


class Percent(models.Model):
    class Meta:
        verbose_name_plural = 'Ботнинг хизмат ҳаққи'
        verbose_name = 'Ботнинг хизмат ҳаққи'

    percent = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.percent}"


class Price(models.Model):
    class Meta:
        verbose_name_plural = 'Категориялар нархи'
        verbose_name = 'Категориялар нархи'

    category = models.ForeignKey(Category, models.CASCADE, related_name='price')
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.price // 1000},000 сўм соатига"
