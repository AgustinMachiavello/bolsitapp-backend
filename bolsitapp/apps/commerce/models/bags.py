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
  name = models.CharField("Bag name", max_length = 30, null = True, blank = True)
  user = models.ForeignKey(User, on_delete = models.PROTECT, null = True, blank = True, related_name='user')
  
  def __str__(self):
    return '#{0} | {1}'.format(self.id_bag, self.qr_code)
  
  class Meta:
    verbose_name = "Bag"
    verbose_name_plural = "Bags"