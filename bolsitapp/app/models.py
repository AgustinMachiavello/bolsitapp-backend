from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
#from django.contrib.gis.db import models

class User(models.Model):
  SEX = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('N/A', 'No Answer'),
  )
  ci = models.PositiveIntegerField(
    "CI", primary_key = True,
    validators = [MaxLengthValidator(8), MinLengthValidator(8)])
  name = models.CharField(
    "Name", max_length = 20, editable = True, null = False)
  last_name = models.CharField(
    "Last Name", max_length = 20,editable = True, null = False)
  email = models.CharField(
    "Email", max_length = 50, editable = True, null = False)
  password = models.CharField(
    "Password", max_length = 20, editable = True, null = False)
  sex = models.CharField(
    "Sex", max_length = 3, choices = SEX, editable = True, null = False)
  phone = models.PositiveIntegerField(
    "Phone Number", editable = True,
    validators = [MaxLengthValidator(11)])
  address = models.CharField(
    "Address", max_length = 50, editable = True)
  postal_code = models.PositiveIntegerField(
    "Postal Code", editable = True, null = False,
    validators = [MaxLengthValidator(5), MinLengthValidator(5)])

  class Meta:
    verbose_name = "User"
    verbose_name_plural = "Users"

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
  
  user = models.ForeignKey(User, on_delete = models.RESTRICT)

  class Meta:
    verbose_name = "Bag"
    verbose_name_plural = "Bags"

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
  
  class Meta:
    verbose_name = "Store"
    verbose_name_plural = "Stores"

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

  class Meta:
    verbose_name = "Purchase"
    verbose_name_plural = "Purchases"

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