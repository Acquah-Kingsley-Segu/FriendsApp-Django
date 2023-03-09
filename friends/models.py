from django.db import models
from django.core import validators

class Friend(models.Model):
  first_name = models.CharField(max_length=500)
  last_name = models.CharField(max_length=500)
  email = models.CharField(max_length=200, unique=True, validators=[validators.EmailValidator()])
  phone = models.CharField(max_length=10, unique=True, validators=[validators.MaxLengthValidator(limit_value=10, message="Enter more than 10 values")])
  twitter_handle = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.last_name + " " + self.first_name

