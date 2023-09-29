# Generated by Django 4.1.7 on 2023-09-24 09:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toifa', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name': 'Права тоифалари',
                'verbose_name_plural': 'Права тоифалари',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('familiya', models.CharField(max_length=255)),
                ('telefon', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed.", regex='^998[378]{2}|9[01345789]\\d{7}$')])),
                ('prava', models.CharField(max_length=15)),
                ('telegram_id', models.BigIntegerField()),
            ],
            options={
                'verbose_name': 'Ўрганувчилар',
                'verbose_name_plural': 'Ўрганувчилар',
            },
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bot_link', models.CharField(max_length=250)),
                ('online_lesson', models.CharField(max_length=250)),
                ('online_lesson_ru', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('text_ru', models.TextField()),
            ],
            options={
                'verbose_name': 'Маълумотлар',
                'verbose_name_plural': 'Маълумотлар',
            },
        ),
        migrations.CreateModel(
            name='TextClientRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=380)),
                ('ism_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('familiya', models.CharField(max_length=380)),
                ('familiya_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('telefon', models.CharField(max_length=380)),
                ('telefon_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('prava', models.CharField(max_length=380)),
                ('prava_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('telefon_qayta', models.CharField(max_length=380)),
                ('telefon_qayta_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('prava_bor', models.CharField(max_length=380)),
                ('prava_bor_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('prava_yuq', models.CharField(max_length=380)),
                ('prava_yuq_ru', models.CharField(blank=True, max_length=380, null=True)),
            ],
            options={
                'verbose_name': 'Техт регистер',
                'verbose_name_plural': 'Техт регистер',
            },
        ),
        migrations.CreateModel(
            name='TextClientUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=380)),
                ('ism_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('familiya', models.CharField(max_length=380)),
                ('familiya_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('telefon', models.CharField(max_length=380)),
                ('telefon_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('prava', models.CharField(max_length=380)),
                ('prava_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('telefon_qayta', models.CharField(max_length=380)),
                ('telefon_qayta_ru', models.CharField(blank=True, max_length=380, null=True)),
            ],
            options={
                'verbose_name': 'Техт изменет',
                'verbose_name_plural': 'Техт изменет',
            },
        ),
    ]