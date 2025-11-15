from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Auto

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'año', 'precio', 'disponible')
    search_fields = ('marca', 'modelo')