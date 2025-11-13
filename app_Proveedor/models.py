# app_Proveedor/models.py

from django.db import models

# --- 1. Modelo Proveedor (7 campos) ---
class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la Empresa") 
    contacto_principal = models.CharField(max_length=100, verbose_name="Contacto Principal") 
    telefono = models.CharField(max_length=15, blank=True, null=True) 
    email = models.EmailField(unique=True) 
    direccion = models.CharField(max_length=200, verbose_name="Dirección") 
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro") 
    activo = models.BooleanField(default=True) 

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['nombre_empresa']

    def __str__(self):
        return self.nombre_empresa

# --- 2. Modelo Distribuidor (7 campos) ---
class Distribuidor(models.Model):
    nombre_distribuidor = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Distribuidor") 
    tipo_servicio = models.CharField(max_length=50, choices=[('LOCAL', 'Local'), ('NACIONAL', 'Nacional'), ('INTERNACIONAL', 'Internacional')]) 
    ciudad = models.CharField(max_length=50) 
    pais = models.CharField(max_length=50) 
    tiempo_entrega_dias = models.IntegerField(verbose_name="Tiempo de Entrega (días)") 
    comision = models.DecimalField(max_digits=5, decimal_places=2, help_text="Comisión en porcentaje") 
    ultima_revision = models.DateField(auto_now=True, verbose_name="Última Revisión") 

    class Meta:
        verbose_name = "Distribuidor"
        verbose_name_plural = "Distribuidores"
        ordering = ['nombre_distribuidor']

    def __str__(self):
        return self.nombre_distribuidor

# --- 3. Modelo Producto (7 campos, incluyendo las relaciones) ---
class Producto(models.Model):
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE,
        related_name='productos_suministrados',
        verbose_name="ID Proveedor" 
    )

    distribuidores = models.ManyToManyField(
        Distribuidor,
        related_name='productos_distribuidos',
        verbose_name="Distribuidores"
    )

    nombre = models.CharField(max_length=150, unique=True, verbose_name="Nombre del Producto") 
    sku = models.CharField(max_length=50, unique=True, verbose_name="SKU/Código") 
    precio = models.DecimalField(max_digits=10, decimal_places=2) 
    stock_actual = models.IntegerField(verbose_name="Stock Actual") 
    descripcion = models.TextField(blank=True, verbose_name="Descripción") 

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    
class Empleado(models.Model):
    # Django automáticamente crea el campo 'id' (Primary Key)
    nombre = models.CharField(max_length=150, verbose_name="Nombre Completo")
    puesto = models.CharField(max_length=100, verbose_name="Puesto/Cargo")
    fecha_ingreso = models.DateField(verbose_name="Fecha de Ingreso") # Usamos DateField para solo la fecha
    salario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salario Mensual")
    edad = models.IntegerField(verbose_name="Edad")

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre Completo")
    email = models.EmailField(max_length=100, unique=True, verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    pais = models.CharField(max_length=50, verbose_name="País")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

# --- 6. Modelo Venta ---
class Venta(models.Model):
    # Relaciones Foreign Key
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name="Cliente")
    id_producto = models.ForeignKey(Producto, on_delete=models.PROTECT, verbose_name="Producto Vendido") 
    
    # Campos de Venta
    cantidad = models.IntegerField(verbose_name="Cantidad Vendida")
    fecha_venta = models.DateField(auto_now_add=True, verbose_name="Fecha de Venta") # auto_now_add=True guarda la fecha automáticamente
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo Total") # 10 dígitos, 2 decimales

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ['-fecha_venta'] # Ordenar de más reciente a más antigua

    def __str__(self):
        return f"Venta {self.id} a {self.id_cliente.nombre} ({self.fecha_venta})"


# --- 7. Modelo Envío ---
class Envio(models.Model):
    # Relación Foreign Key
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name="Cliente")
    
    # Campos de Envío
    fecha_envio = models.DateField(auto_now_add=True, verbose_name="Fecha de Envío")
    estado = models.CharField(max_length=50, choices=[
        ('PENDIENTE', 'Pendiente'),
        ('EN_CAMINO', 'En Camino'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado'),
    ], default='PENDIENTE', verbose_name="Estado del Envío")
    pais = models.CharField(max_length=50, verbose_name="País de Destino")
    direccion = models.CharField(max_length=255, verbose_name="Dirección de Destino")

    class Meta:
        verbose_name = "Envío"
        verbose_name_plural = "Envíos"
        ordering = ['fecha_envio']

    def __str__(self):
        return f"Envío {self.id} a {self.id_cliente.nombre} ({self.estado})"