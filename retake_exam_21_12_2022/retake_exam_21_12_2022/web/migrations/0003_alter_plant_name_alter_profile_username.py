# Generated by Django 4.1.4 on 2022-12-21 07:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_plant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Username'),
        ),
    ]
