from distutils.command import register
from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Brand)
class Admin(admin.ModelAdmin):
    pass


@admin.register(models.Brochure)
class Admin(admin.ModelAdmin):
    pass

@admin.register(models.Country)
class Admin(admin.ModelAdmin):
    pass

@admin.register(models.City)
class Admin(admin.ModelAdmin):
    pass
