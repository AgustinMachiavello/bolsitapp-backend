from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator

from ...accounts.models import User
from ..models.branches import Branch

class Exchange(models.Model):
  date = models.DateTimeField(
    "Date", auto_now_add = True)
  eco_points = models.PositiveIntegerField(
    "EcoPoints", null = False)
  
  store_branch = models.ForeignKey(Branch, on_delete = models.RESTRICT)
  user = models.ForeignKey(User, on_delete = models.RESTRICT)
  
  class Meta:
    unique_together = ('user' , 'date')
    verbose_name = "Exchange"
    verbose_name_plural = "Exchanges"