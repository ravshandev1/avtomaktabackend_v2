# Generated by Django 4.1.7 on 2023-09-28 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='client',
        ),
        migrations.RemoveField(
            model_name='session',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='session',
            name='moshina',
        ),
        migrations.DeleteModel(
            name='TextSes',
        ),
        migrations.DeleteModel(
            name='Session',
        ),
    ]
