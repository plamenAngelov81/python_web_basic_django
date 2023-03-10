# Generated by Django 4.1.4 on 2022-12-21 09:38

import django.core.validators
from django.db import migrations, models
import retake_exam_21_12_2022.web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_plant_name_alter_profile_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plant',
            options={'ordering': ['pk']},
        ),
        migrations.AlterField(
            model_name='plant',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), retake_exam_21_12_2022.web.models.only_letters_validator], verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='plant_type',
            field=models.CharField(choices=[('Outdoor Plants', 'Outdoor Plants'), ('Indoor Plants', 'Indoor Plants')], max_length=14, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=20, validators=[retake_exam_21_12_2022.web.models.capital_letter_validator], verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=20, validators=[retake_exam_21_12_2022.web.models.capital_letter_validator], verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.URLField(blank=True, null=True, verbose_name='Profile Picture'),
        ),
    ]
