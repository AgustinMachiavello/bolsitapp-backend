from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator


class Store(models.Model):
  CATEGORY = (
    ('S', 'Supermarket'),
    ('P', 'Perfumery'),
    ('D', 'Department Store'),
    ('G', 'Gift Shop'),
  )
  id_store = models.AutoField(
    primary_key = True)
  name = models.CharField(
    "Name", max_length = 20, editable = True, null = False)
  category = models.CharField(
    "Category", max_length = 20, choices = CATEGORY, editable = True, null = False)

  def __str__(self):
    return '#{0} {1}'.format(self.id_store, self.name)

  class Meta:
    verbose_name = "Store"
    verbose_name_plural = "Stores"