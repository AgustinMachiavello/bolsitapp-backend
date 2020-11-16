from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator

from ...accounts.models import User

class Bag(models.Model):
  TYPE = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
  )
  id_bag = models.AutoField(
    primary_key = True)
  qr_code = models.CharField(
    "OR Code", null = False, unique = True, max_length = 50)
  date_registered = models.DateTimeField(
    auto_now_add = True)
  date_discarded = models.DateTimeField(
    "Date Discarded")
  bag_type = models.CharField(
    "Type", max_length = 1, choices = TYPE, null = False)
  
  user = models.ForeignKey(User, on_delete = models.RESTRICT, related_name='user')

  class Meta:
    verbose_name = "Bag"
    verbose_name_plural = "Bags"