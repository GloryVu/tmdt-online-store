from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.ClothesBrand)
admin.site.register(models.Clothes)
admin.site.register(models.ClothesItem)
admin.site.register(models.ClothesStats)
