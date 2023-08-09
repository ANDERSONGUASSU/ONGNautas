# Generated by Django 4.2.3 on 2023-08-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=24, verbose_name='title')),
                ('short_description', models.CharField(max_length=64, verbose_name='short description')),
                ('description', models.TextField(verbose_name='description')),
                ('address', models.CharField(max_length=50, verbose_name='address')),
                ('image', models.ImageField(upload_to='projects', verbose_name='image')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('amount_spent', models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='amount spent')),
            ],
        ),
    ]