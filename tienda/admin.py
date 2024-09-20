from django.contrib import admin

# Register your models here.
from .models import Categoria, Producto, Cliente

@admin.action(description='Establecer stock a 20 unidades')
def establecer_stock_a_20(modeladmin, request, queryset):
    queryset.update(stock=20)

class Producto20(admin.ModelAdmin):
    list_display = ('nombre', 'stock')
    actions = [establecer_stock_a_20]

admin.site.register(Categoria)
admin.site.register(Producto, Producto20)
admin.site.register(Cliente)