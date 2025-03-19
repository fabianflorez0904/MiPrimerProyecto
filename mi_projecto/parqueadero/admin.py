from django.contrib import admin
from .models import Parqueadero

# Register your models here.


@admin.register(Parqueadero)
class ParqueaderoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad', 'ubicacion')
    search_field = ('nombre', 'ubicacion')
