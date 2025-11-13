# app_Proveedor/urls.py (Versión Corregida y Completa)

from django.urls import path
from . import views

urlpatterns = [
    # ... (Rutas de Proveedor existentes)
    path('', views.inicio_proveedor, name='ver_proveedores'), 
    path('inicio/', views.inicio_sistema, name='inicio'), 
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/actualizar/<int:pk>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/guardar_actualizacion/<int:pk>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedor/borrar/<int:pk>/', views.borrar_proveedor, name='borrar_proveedor'),

    # ----------------- CRUD Distribuidor -----------------
    path('distribuidor/', views.inicio_distribuidor, name='ver_distribuidores'), 
    path('distribuidor/agregar/', views.agregar_distribuidor, name='agregar_distribuidor'),
    path('distribuidor/actualizar/<int:pk>/', views.actualizar_distribuidor, name='actualizar_distribuidor'),
    path('distribuidor/guardar_actualizacion/<int:pk>/', views.actualizar_distribuidor, name='realizar_actualizacion_distribuidor'),
    path('distribuidor/borrar/<int:pk>/', views.borrar_distribuidor, name='borrar_distribuidor'),

    path('producto/', views.inicio_producto, name='ver_productos'), 
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/actualizar/<int:pk>/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/guardar_actualizacion/<int:pk>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
    path('producto/borrar/<int:pk>/', views.borrar_producto, name='borrar_producto'),

    path('empleados/', views.ver_empleados, name='ver_empleados'),
    path('empleado/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleado/actualizar/<int:pk>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleado/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('empleado/borrar/<int:pk>/', views.borrar_empleado, name='borrar_empleado'),

    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/actualizar/<int:pk>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('cliente/borrar/<int:pk>/', views.borrar_cliente, name='borrar_cliente'),

    path('ventas/', views.ver_ventas, name='ver_ventas'),
    path('venta/agregar/', views.agregar_venta, name='agregar_venta'),
    path('venta/actualizar/<int:pk>/', views.actualizar_venta, name='actualizar_venta'),
    path('venta/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_venta, name='realizar_actualizacion_venta'),
    path('venta/borrar/<int:pk>/', views.borrar_venta, name='borrar_venta'),
    
    path('envios/', views.ver_envios, name='ver_envios'),
    path('envio/agregar/', views.agregar_envio, name='agregar_envio'),
    path('envio/actualizar/<int:pk>/', views.actualizar_envio, name='actualizar_envio'),
    path('envio/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_envio, name='realizar_actualizacion_envio'),
    path('envio/borrar/<int:pk>/', views.borrar_envio, name='borrar_envio'),
]