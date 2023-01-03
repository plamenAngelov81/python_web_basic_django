from django.db import models
from django.core.validators import MinLengthValidator, ValidationError, MinValueValidator

# Check the validators first!
def validate_username(value):
    for ch in value:
        if not ch.isalpha or not ch == "_": 
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    USERNAME_MAX_LEN = 15
    USERNAME_MIN_LEN = 2
    MIN_AGE_VALUE = 0

    username = models.CharField(
        verbose_name='Username',
        max_length=USERNAME_MAX_LEN,
        validators=[MinLengthValidator(USERNAME_MIN_LEN), validate_username]
    )

    email = models.EmailField(
        verbose_name='Email'
    )

    age = models.IntegerField(
        verbose_name='Age',
        validators=[MinValueValidator(MIN_AGE_VALUE)]
    )


ALBUM_CHOICES = (
    ("Pop Music", "Pop Music"),
    ("Jazz Music", "Jazz Music"),
    ("R&B Music", "R&B Music"),
    ("Rock Music", "Rock Music"),
    ("Country Music", "Country Music"),
    ("Dance Music", "Dance Music"),
    ("Hip Hop Music", "Hip Hop Music"),
    ("Other", "Other"),
)


class Album(models.Model):
    ALBUM_NAME_MAX_LEN = 30
    ARTIST_MAX_LEN = 30
    GENRE_MAX_LEN = 30
    MIN_PRICE_VALUE = 0

    album_name = models.CharField(
        verbose_name='Album_name',
        max_length=ALBUM_NAME_MAX_LEN,
        unique=True
    )

    artist = models.CharField(
        verbose_name='Artist',
        max_length=ARTIST_MAX_LEN,
    )

    genre = models.CharField(
        verbose_name='Genre',
        max_length=GENRE_MAX_LEN,
        choices=ALBUM_CHOICES,
    )

    description = models.TextField(
        verbose_name='Description',
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        verbose_name='Image URL'
    )

    price = models.FloatField(
        verbose_name="Price",
        validators=[MinValueValidator(MIN_PRICE_VALUE)]
    )

    class Meta:
        ordering = ['pk']
