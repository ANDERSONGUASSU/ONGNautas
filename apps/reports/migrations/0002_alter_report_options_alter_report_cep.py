# Generated by Django 4.2.3 on 2023-08-07 13:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'verbose_name': 'Denúncia', 'verbose_name_plural': 'Denúncias'},
        ),
        migrations.AlterField(
            model_name='report',
            name='cep',
            field=models.CharField(default='Sem CEP', max_length=11, validators=[django.core.validators.RegexValidator(message='Insert a valid CEP', regex='\\d{5}-?\\d{3}')]),
        ),
    ]