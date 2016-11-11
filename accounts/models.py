import uuid
from django.db import models
from django.contrib import auth

auth.signals.user_logged_in.disconnect(auth.models.update_last_login)


class User(models.Model):
    email = models.EmailField(primary_key=True)
    REQUIRED_FIELDS = ()
    USERNAME_FIELD = 'email'

    is_authenticated = True
    is_anonymous = False


class Token(models.Model):
    email = models.EmailField(null=True)
    uid = models.CharField(max_length=40, default=uuid.uuid4)

