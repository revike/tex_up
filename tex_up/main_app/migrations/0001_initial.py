# Generated by Django 4.1.3 on 2022-11-20 16:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128, verbose_name='имя')),
                ('phone', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+1?\\d{11,11}$')], verbose_name='телефон')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'db_table': 'client',
            },
        ),
    ]
