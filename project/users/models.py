from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Changing Default username field of type CharField to EmailField
    # Thus we can use the username field as username and email name.
    username = models.EmailField(unique=True, error_messages={'unique': "A user with that username already exists."})

    EMAIL_FIELD = 'username'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def register_user(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

        self.is_superuser = True
        self.is_staff = True

        self.save()
