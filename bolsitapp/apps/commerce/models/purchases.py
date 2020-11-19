from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator

from ..models.bags import Bag
from ..models.branches import Branch


class Purchase(models.Model):
  id_purchase = models.AutoField(
    primary_key = True)
  date = models.DateTimeField(
    "Date", auto_now_add = True)
  eco_points = models.PositiveIntegerField(
    "EcoPoints", null = False)
  total = models.DecimalField(
    "Purchase Total", max_digits = 8, decimal_places = 2, null = False)
  
  bag = models.ForeignKey(Bag, on_delete = models.RESTRICT)
  store_branch = models.ForeignKey(Branch, on_delete = models.RESTRICT)

  def __str__(self):
    return '#{0} | {1}'.format(self.id_purchase, self.store_branch.store.name)

  class Meta:
    verbose_name = "Purchase"
    verbose_name_plural = "Purchases"