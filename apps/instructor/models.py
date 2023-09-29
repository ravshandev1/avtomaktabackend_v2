from django.db import models
from client.models import phone_regex
from django.core.validators import RegexValidator
from session.models import Category

car_number = RegexValidator(
    regex='^[0-9]{1}[0-5]{1}[ -][A-Z]{1}[ -][0-9]{3}[ -][A-Z]{2}$',
    message="Car number must be entered in the format: '[XX] [X] [XXX] [XX]'. Up to 8 characters allowed."
)
car_number2 = RegexValidator(
    regex='^[0-9]{1}[0-5]{1}[ -][0-9]{3}[ -][A-Z]{3}$',
    message="Car number must be entered in the format: '[XX] [XXX] [XXX]'. Up to 8 characters allowed."
)


class Tuman(models.Model):
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Туманлар'
        verbose_name = 'Туманлар'


class Instructor(models.Model):
    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    telefon = models.CharField(validators=[phone_regex], max_length=12)
    tuman = models.CharField(max_length=255, null=True)
    toifa = models.ManyToManyField(Category, related_name='instructors')
    moshina = models.CharField(max_length=255, null=True)
    nomeri = models.CharField(max_length=11)
    telegram_id = models.BigIntegerField()
    tasdiqlash = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ism} {self.moshina}"

    class Meta:
        verbose_name_plural = 'Инструкторлар'
        verbose_name = 'Инструкторлар'


class TextInsRegister(models.Model):
    ism = models.CharField(max_length=380)
    ism_ru = models.CharField(max_length=380, null=True, blank=True)
    familiya = models.CharField(max_length=380)
    familiya_ru = models.CharField(max_length=380, null=True, blank=True)
    telefon = models.CharField(max_length=380)
    telefon_ru = models.CharField(max_length=380, null=True, blank=True)
    telefon_qayta = models.CharField(max_length=380)
    telefon_qayta_ru = models.CharField(max_length=380, null=True, blank=True)
    manzil = models.CharField(max_length=380)
    manzil_ru = models.CharField(max_length=380, null=True, blank=True)
    categoriya = models.CharField(max_length=380)
    categoriya_ru = models.CharField(max_length=380, null=True, blank=True)
    moshina = models.CharField(max_length=380)
    moshina_ru = models.CharField(max_length=380, null=True, blank=True)
    moshina_nomeri = models.CharField(max_length=380)
    moshina_nomeri_ru = models.CharField(max_length=380, null=True, blank=True)
    moshina_nomeri_qayta = models.CharField(max_length=380)
    moshina_nomeri_qayta_ru = models.CharField(max_length=380, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Техт Инструктор Регистер'
        verbose_name = 'Техт Инструктор Регистер'


class TextInsUpdater(models.Model):
    ism = models.CharField(max_length=380)
    ism_ru = models.CharField(max_length=380, null=True, blank=True)
    familiya = models.CharField(max_length=380)
    familiya_ru = models.CharField(max_length=380, null=True, blank=True)
    telefon = models.CharField(max_length=380)
    telefon_ru = models.CharField(max_length=380, null=True, blank=True)
    telefon_qayta = models.CharField(max_length=380)
    telefon_qayta_ru = models.CharField(max_length=380, null=True, blank=True)
    manzil = models.CharField(max_length=380)
    manzil_ru = models.CharField(max_length=380, null=True, blank=True)
    categoriya = models.CharField(max_length=380)
    categoriya_ru = models.CharField(max_length=380, null=True, blank=True)
    moshina = models.CharField(max_length=380)
    moshina_ru = models.CharField(max_length=380, null=True, blank=True)
    moshina_nomeri = models.CharField(max_length=380)
    moshina_nomeri_ru = models.CharField(max_length=380, null=True, blank=True)
    moshina_nomeri_qayta = models.CharField(max_length=380)
    moshina_nomeri_qayta_ru = models.CharField(max_length=380, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Техт Инструктор Изменет'
        verbose_name = 'Техт Инструктор Изменет'
