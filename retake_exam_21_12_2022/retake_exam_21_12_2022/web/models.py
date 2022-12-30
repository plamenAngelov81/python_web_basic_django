from django.db import models
from django.core.validators import MinLengthValidator, ValidationError


def capital_letter_validator(some_string: str):
    if not some_string[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


def only_letters_validator(some_string: str):
    for ch in some_string:
        if not ch.isalpha():
            raise ValidationError("Plant name should contain only letters!")


class Profile(models.Model):
    username = models.CharField(
        verbose_name='Username',
        max_length=10,
        validators=[MinLengthValidator(2)]
    )

    first_name = models.CharField(
        verbose_name='First Name',
        max_length=20,
        validators=[capital_letter_validator]
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=20,
        validators=[capital_letter_validator]
    )

    profile_picture = models.URLField(
        verbose_name='Profile Picture',
        null=True,
        blank=True
    )


PLANT_TYPE = (
    ('Outdoor Plants', 'Outdoor Plants'),
    ('Indoor Plants', 'Indoor Plants'),
)


class Plant(models.Model):
    plant_type = models.CharField(
        verbose_name="Type",
        max_length=14,
        choices=PLANT_TYPE,
    )

    name = models.CharField(
        verbose_name='Name',
        max_length=20,
        validators=[MinLengthValidator(2), only_letters_validator]
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )

    description = models.TextField(
        verbose_name='Description',
    )

    price = models.FloatField(
        verbose_name='Price'
    )

    class Meta:
        ordering = ['pk']
