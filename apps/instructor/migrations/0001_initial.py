# Generated by Django 4.1.7 on 2023-09-24 09:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('familiya', models.CharField(max_length=255)),
                ('telefon', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed.", regex='^998[378]{2}|9[01345789]\\d{7}$')])),
                ('jins', models.CharField(max_length=15)),
                ('tuman', models.CharField(max_length=255, null=True)),
                ('moshina', models.CharField(max_length=255, null=True)),
                ('nomeri', models.CharField(max_length=11)),
                ('balans', models.IntegerField(default=0)),
                ('telegram_id', models.BigIntegerField()),
                ('ratet', models.PositiveIntegerField(default=1)),
                ('location', models.CharField(max_length=250, null=True)),
                ('card', models.CharField(max_length=15)),
                ('tasdiqlash', models.BooleanField(default=False)),
                ('toifa', models.ManyToManyField(related_name='instructors', to='client.category')),
            ],
            options={
                'verbose_name': 'Инструкторлар',
                'verbose_name_plural': 'Инструкторлар',
                'ordering': ['-ratet'],
            },
        ),
        migrations.CreateModel(
            name='TextInsRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=380)),
                ('ism_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('familiya', models.CharField(max_length=380)),
                ('familiya_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('telefon', models.CharField(max_length=380)),
                ('telefon_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('jins', models.CharField(max_length=380)),
                ('jins_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('telefon_qayta', models.CharField(max_length=380)),
                ('telefon_qayta_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('manzil', models.CharField(max_length=380)),
                ('manzil_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('categoriya', models.CharField(max_length=380)),
                ('categoriya_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('moshina', models.CharField(max_length=380)),
                ('moshina_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('moshina_nomeri', models.CharField(max_length=380)),
                ('moshina_nomeri_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('moshina_nomeri_qayta', models.CharField(max_length=380)),
                ('moshina_nomeri_qayta_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('lacatsiya', models.CharField(max_length=380)),
                ('lacatsiya_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('karta', models.CharField(max_length=380)),
                ('karta_ru', models.CharField(blank=True, max_length=380, null=True)),
            ],
            options={
                'verbose_name': 'Техт Инструктор Регистер',
                'verbose_name_plural': 'Техт Инструктор Регистер',
            },
        ),
        migrations.CreateModel(
            name='TextInsUpdater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=380)),
                ('ism_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('familiya', models.CharField(max_length=380)),
                ('familiya_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('telefon', models.CharField(max_length=380)),
                ('telefon_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('telefon_qayta', models.CharField(max_length=380)),
                ('telefon_qayta_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('manzil', models.CharField(max_length=380)),
                ('manzil_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('categoriya', models.CharField(max_length=380)),
                ('categoriya_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('moshina', models.CharField(max_length=380)),
                ('moshina_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('moshina_nomeri', models.CharField(max_length=380)),
                ('moshina_nomeri_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('moshina_nomeri_qayta', models.CharField(max_length=380)),
                ('moshina_nomeri_qayta_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('lacatsiya', models.CharField(max_length=380)),
                ('lacatsiya_ru', models.CharField(blank=True, max_length=380, null=True)),
                ('karta', models.CharField(max_length=380)),
                ('karta_ru', models.CharField(blank=True, max_length=380, null=True)),
            ],
            options={
                'verbose_name': 'Техт Инструктор Изменет',
                'verbose_name_plural': 'Техт Инструктор Изменет',
            },
        ),
        migrations.CreateModel(
            name='Tuman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Туманлар',
                'verbose_name_plural': 'Туманлар',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rating', to='client.client')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='instructor.instructor')),
            ],
            options={
                'verbose_name': 'Инструкторлар рейтинги',
                'verbose_name_plural': 'Инструкторлар рейтинги',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summa', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('instructor', models.ForeignKey(on_delete=models.SET('Инструктор ўчиб кетган'), related_name='payments', to='instructor.instructor')),
            ],
            options={
                'verbose_name': 'Тўловлар',
                'verbose_name_plural': 'Тўловлар',
            },
        ),
    ]
