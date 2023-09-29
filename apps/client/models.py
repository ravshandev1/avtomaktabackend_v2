from django.core.validators import RegexValidator
from django.db import models

phone_regex = RegexValidator(
    regex=r"^998[378]{2}|9[01345789]\d{7}$",
    message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)


class Information(models.Model):
    class Meta:
        verbose_name = 'Маълумотлар'
        verbose_name_plural = 'Маълумотлар'

    bot_link = models.CharField(max_length=250)
    online_lesson = models.TextField()
    online_lesson_ru = models.TextField()
    text = models.TextField()
    text_ru = models.TextField()

    def __str__(self):
        return self.bot_link


class Category(models.Model):
    class Meta:
        verbose_name = 'Права тоифалари'
        verbose_name_plural = 'Права тоифалари'

    toifa = models.CharField(max_length=2)

    def __str__(self):
        return self.toifa
