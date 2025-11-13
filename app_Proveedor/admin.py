# app_Proveedor/admin.py

from django.contrib import admin
from .models import Proveedor, Distribuidor, Producto

# Registro de Proveedor
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre_empresa', 'email', 'telefono', 'activo', 'fecha_registro')
    search_fields = ('nombre_empresa', 'email')
    list_filter = ('activo', 'fecha_registro')

# Registro de Distribuidor (Pendiente de uso en vistas, pero registrado)
@admin.register(Distribuidor)
class DistribuidorAdmin(admin.ModelAdmin):
    list_display = ('nombre_distribuidor', 'tipo_servicio', 'ciudad', 'ultima_revision')
    list_filter = ('tipo_servicio', 'pais')

# Registro de Producto (Pendiente de uso en vistas, pero registrado)
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sku', 'precio', 'stock_actual', 'proveedor')
    list_filter = ('proveedor', 'distribuidores')
    search_fields = ('nombre', 'sku')
    filter_horizontal = ('distribuidores',) # Mejor widget para ManyToMany