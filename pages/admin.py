from django.contrib import admin

from .models import *

admin.site.register(Material)
admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(ProductMaterial)