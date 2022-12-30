from django.db import models
from django.core.validators import ValidationError, MinValueValidator, MinLengthValidator


TYPE_CHOICES = (
    ("Sports Car", "Sports Car"),
    ("Pickup", "Pickup"),
    ("Crossover", "Crossover"),
    ("Minibus", "Minibus"),
    ("Other", "Other")
)


def user_name_min_length(value):
    if len(value) < 2:
        raise ValidationError('The username must be a minimum of 2 chars')


def car_year_range(value):
    if not 1980 <= value <= 2049:
        raise ValidationError("Year must be between 1980 and 2049")


class Profile(models.Model):
    USER_NAME_MAX_LEN = 10
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30
    PASSWORD_MAX_LEN = 30
    MIN_AGE = 18

    user_name = models.CharField(
        verbose_name='Username',
        max_length=USER_NAME_MAX_LEN,
        null=False,
        blank=False,
        validators=[user_name_min_length]
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(MIN_AGE)]
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
        null=False,
        blank=False
    )

    first_name = models.CharField(
        verbose_name='First Name',
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=True
    )

    profile_picture = models.URLField(
        verbose_name='Profile Picture',
        null=True,
        blank=True
    )

    @property
    def full_name(self):
        first = ""
        last = ''
        if self.first_name:
            first = self.first_name
        if self.last_name:
            last = self.last_name
        return f"{first} {last}"


class Car(models.Model):
    TYPE_MAX_LEN = 10
    MODEL_MAX_LEN = 20
    MODEL_MIN_LEN = 2
    PRICE_MIN_VALUE = 1

    type = models.CharField(
        max_length=TYPE_MAX_LEN,
        choices=TYPE_CHOICES,
        null=False,
        blank=False
    )

    model = models.CharField(
        max_length=MODEL_MAX_LEN,
        null=False,
        blank=False,
        validators=[MinLengthValidator(MODEL_MIN_LEN)]
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[car_year_range]
    )

    image_url = models.URLField(
        verbose_name='Image URL',
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(PRICE_MIN_VALUE)]
    )

    class Meta:
        ordering = ['pk']
