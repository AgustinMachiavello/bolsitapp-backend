from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  SEX = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('N/A', 'No Answer'),
  )
  ci = models.PositiveIntegerField("CI", primary_key = True)
  name = models.CharField(
    "Name", max_length = 20, editable = True, null = False)
  last_name = models.CharField(
    "Last Name", max_length = 20,editable = True, null = False)
  email = models.CharField(
    "Email", max_length = 50, editable = True, null = False, unique = True)
  sex = models.CharField(
    "Sex", max_length = 3, choices = SEX, editable = True, null = False)
  phone = models.PositiveIntegerField(
    "Phone Number", editable = True)
  address = models.CharField(
    "Address", max_length = 50, editable = True)
  postal_code = models.PositiveIntegerField(
    "Postal Code", editable = True, null = False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = [
    'ci', 'username', 'name', 'last_name', 'sex', 'phone', 'address', 'postal_code']

  class Meta:
    verbose_name = "User"
    verbose_name_plural = "Users"