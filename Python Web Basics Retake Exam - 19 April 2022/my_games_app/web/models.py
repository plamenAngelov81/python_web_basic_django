from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    MIN_AGE_VALUE = 12
    PASSWORD_MAX_LEN = 30
    FIRS_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    email = models.EmailField(
        verbose_name='Email',
    )

    age = models.IntegerField(
        verbose_name="Age",
        validators=[MinValueValidator(MIN_AGE_VALUE)]
    )

    password = models.CharField(
        verbose_name='Password',
        max_length=PASSWORD_MAX_LEN
    )

    first_name = models.CharField(
        verbose_name='First Name',
        max_length=FIRS_NAME_MAX_LEN,
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
        null=True,
        blank=True,
        verbose_name='Profile Picture'
    )

    class Meta:
        verbose_name_plural = 'Profile'

    def full_name(self):
        first = ''
        last = ''
        if self.first_name:
            first = self.first_name
        if self.last_name:
            last = self.last_name
        return f"{first} {last}"



CATEGORY_CHOICES = (
    ("Action", "Action"),
    ("Adventure", "Adventure"),
    ("Puzzle", "Puzzle"),
    ("Strategy", "Strategy"),
    ("Sports", "Sports"),
    ("Board/Card Game", "Board/Card game"),
    ("Other", "Other"),
)


class Game(models.Model):
    TITLE_MAX_LEN = 30
    CATEGORY_MAX_LEN = 15
    MAX_RATING = 5
    MIN_RATING = 0.1
    MIN_LEVEL_VALUE = 1

    title = models.CharField(
        verbose_name='Title',
        unique=True,
        max_length=TITLE_MAX_LEN
    )

    category = models.CharField(
        verbose_name='Category',
        choices=CATEGORY_CHOICES,
        max_length=CATEGORY_MAX_LEN
    )

    rating = models.FloatField(
        verbose_name='Rating',
        validators=[MinValueValidator(MIN_RATING), MaxValueValidator(MAX_RATING)]
    )

    max_level = models.IntegerField(
        verbose_name='Max Level',
        validators=[MinValueValidator(MIN_LEVEL_VALUE)],
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )

    summary = models.TextField(
        verbose_name='Summary',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['pk']
