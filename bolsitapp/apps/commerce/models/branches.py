from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator

from ..models.stores import Store

class Branch(models.Model):
  id_branch = models.AutoField(
    primary_key = True)  
  address = models.CharField(
    "Address", max_length = 50, editable = True, null = False)
  #location = models.PointField(
  #  "Location", null = False)
  
  store = models.ForeignKey(Store, on_delete = models.RESTRICT)

  class Meta:
    verbose_name = "Branch"
    verbose_name_plural = "Branches"