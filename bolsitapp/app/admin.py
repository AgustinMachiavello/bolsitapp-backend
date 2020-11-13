from django.contrib import admin
from bolsitapp.app.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Bag)
admin.site.register(Store)
admin.site.register(Branch)
admin.site.register(Purchase)
admin.site.register(Exchange)