from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    # full_name = models.CharField(max_length=100, blank=True, null=True)
    # phone_number = models.CharField(max_length=100, blank=True, null=True)
    # avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    email = models.EmailField(max_length=100, unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [ "email" ]

    def __str__(self):
        return self.username