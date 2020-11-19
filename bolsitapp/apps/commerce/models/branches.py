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
  latitude = models.FloatField("Latitude", null = False)
  longitude = models.FloatField("Longitude", null = False)
  store = models.ForeignKey(Store, on_delete = models.RESTRICT, related_name='store')
  imageURL = models.URLField("imageURL", null = True)
  openTime = models.TimeField("Open time", null = True)
  closeTime = models.TimeField("Close time", null = True)
  description = models.CharField("Description", max_length=100, null = True)

  def __str__(self):
    return '#{0} | Store: {1}'.format(self.id_branch, self.store.name)

  class Meta:
    verbose_name = "Branch"
    verbose_name_plural = "Branches"