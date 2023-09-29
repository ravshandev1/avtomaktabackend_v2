# Generated by Django 4.1.7 on 2023-09-28 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='client',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='instructor',
        ),
        migrations.AlterModelOptions(
            name='instructor',
            options={'verbose_name': 'Инструкторлар', 'verbose_name_plural': 'Инструкторлар'},
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='balans',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='card',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='jins',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='location',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='ratet',
        ),
        migrations.RemoveField(
            model_name='textinsregister',
            name='jins',
        ),
        migrations.RemoveField(
            model_name='textinsregister',
            name='jins_ru',
        ),
        migrations.RemoveField(
            model_name='textinsregister',
            name='karta',
        ),
        migrations.RemoveField(
            model_name='textinsregister',
            name='karta_ru',
        ),
        migrations.RemoveField(
            model_name='textinsregister',
            name='lacatsiya',
        ),
        migrations.RemoveField(
            model_name='textinsregister',
            name='lacatsiya_ru',
        ),
        migrations.RemoveField(
            model_name='textinsupdater',
            name='karta',
        ),
        migrations.RemoveField(
            model_name='textinsupdater',
            name='karta_ru',
        ),
        migrations.RemoveField(
            model_name='textinsupdater',
            name='lacatsiya',
        ),
        migrations.RemoveField(
            model_name='textinsupdater',
            name='lacatsiya_ru',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]