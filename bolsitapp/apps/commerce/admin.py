from django.contrib import admin
from .models import (
    Bag,
    Branch,
    Exchange,
    Purchase,
    Store
)

# Register your models here.
admin.site.register(Bag)
admin.site.register(Branch)
admin.site.register(Exchange)
admin.site.register(Purchase)
admin.site.register(Store)
