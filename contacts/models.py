from django.db import models
from django.core.validators import RegexValidator

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    email = models.EmailField(unique=True )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
