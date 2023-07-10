from django.contrib import admin

from .models import Vehiculo

# Register your models here.
# class VehiculoAdmin(admin.ModelAdmin):
#     readonly_fields = ('created', 'updated')

class VehiculoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    search_fields = ('marca', 'modelo', 'categoria')
    ordering = ('modelo', )

admin.site.register(Vehiculo, VehiculoAdmin)