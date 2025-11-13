# app_Proveedor/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor, Distribuidor, Producto, Empleado, Cliente, Venta, Envio # Solo trabajaremos con Proveedor por ahora
from django.db import IntegrityError # Para manejar errores de unique

# ----------------- Funciones para PROVEEDOR ------------------------------------------------------------
# [0] INICIO DEL SISTEMA (Muestra el inicio.html)
def inicio_sistema(request):
    """Muestra la página de inicio/bienvenida del sistema."""
    return render(request, 'inicio.html')

# [1] INICIO PROVEEDOR (Muestra la tabla de proveedores)
def inicio_proveedor(request):
    """Muestra la lista de proveedores."""
    proveedores = Proveedor.objects.all().order_by('nombre_empresa')
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})


# [2] AGREGAR PROVEEDOR (GET y POST)
def agregar_proveedor(request):
    if request.method == 'POST':
        # Captura de datos del formulario POST (sin forms.py)
        try:
            Proveedor.objects.create(
                nombre_empresa=request.POST.get('nombre_empresa'),
                contacto_principal=request.POST.get('contacto_principal'),
                telefono=request.POST.get('telefono'),
                email=request.POST.get('email'),
                direccion=request.POST.get('direccion'),
                activo=request.POST.get('activo') == 'on' # Checkbox activo
            )
            # Redirigir a la lista de proveedores después de agregar
            return redirect('ver_proveedores')
        except IntegrityError:
            # Manejo básico de datos duplicados (e.g., email o nombre_empresa)
            contexto = {'error': 'Error: El Nombre de la Empresa o Email ya existe.', 'es_post': True}
            return render(request, 'proveedor/agregar_proveedor.html', contexto)
        except Exception as e:
             contexto = {'error': f'Error al guardar: {e}', 'es_post': True}
             return render(request, 'proveedor/agregar_proveedor.html', contexto)
    
    # Si es GET, simplemente renderiza el formulario
    return render(request, 'proveedor/agregar_proveedor.html')


# [3] ACTUALIZAR PROVEEDOR (GET - Muestra el formulario con datos actuales)
def actualizar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})


# [4] REALIZAR ACTUALIZACION PROVEEDOR (POST - Guarda los cambios)
def realizar_actualizacion_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    
    if request.method == 'POST':
        try:
            proveedor.nombre_empresa = request.POST.get('nombre_empresa')
            proveedor.contacto_principal = request.POST.get('contacto_principal')
            proveedor.telefono = request.POST.get('telefono')
            proveedor.email = request.POST.get('email')
            proveedor.direccion = request.POST.get('direccion')
            proveedor.activo = request.POST.get('activo') == 'on' # Checkbox activo
            
            # Guardar en la BD
            proveedor.save()
            return redirect('ver_proveedores')
        except IntegrityError:
            contexto = {'error': 'Error: El Nombre de la Empresa o Email ya existe.', 'proveedor': proveedor}
            return render(request, 'proveedor/actualizar_proveedor.html', contexto)
        except Exception as e:
            contexto = {'error': f'Error al actualizar: {e}', 'proveedor': proveedor}
            return render(request, 'proveedor/actualizar_proveedor.html', contexto)
    
    return redirect('ver_proveedores') # Si no es POST, regresa a la lista


# [5] BORRAR PROVEEDOR (GET - Muestra confirmación/se utiliza como acción directa)
def borrar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
        
    # Si es GET, muestra la página de confirmación
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})

# [6] INICIO/VER DISTRIBUIDOR-----------------------------------------------------------------------------------------------
def inicio_distribuidor(request):
    """Muestra la lista de distribuidores."""
    distribuidores = Distribuidor.objects.all().order_by('nombre_distribuidor')
    # Usamos un nuevo template para mostrar la tabla
    return render(request, 'distribuidor/ver_distribuidores.html', {'distribuidores': distribuidores})

# [7] AGREGAR DISTRIBUIDOR (GET y POST)
def agregar_distribuidor(request):
    if request.method == 'POST':
        try:
            # Captura de datos del formulario POST (sin forms.py)
            Distribuidor.objects.create(
                nombre_distribuidor=request.POST.get('nombre_distribuidor'),
                tipo_servicio=request.POST.get('tipo_servicio'),
                ciudad=request.POST.get('ciudad'),
                pais=request.POST.get('pais'),
                tiempo_entrega_dias=request.POST.get('tiempo_entrega_dias'),
                comision=request.POST.get('comision')
            )
            return redirect('ver_distribuidores')
        except IntegrityError:
            contexto = {'error': 'Error: El Nombre del Distribuidor ya existe.', 'es_post': True}
            return render(request, 'distribuidor/agregar_distribuidor.html', contexto)
    
    # Si es GET, simplemente renderiza el formulario
    return render(request, 'distribuidor/agregar_distribuidor.html')


# [8] ACTUALIZAR DISTRIBUIDOR (GET - Muestra el formulario con datos actuales)
def actualizar_distribuidor(request, pk):
    distribuidor = get_object_or_404(Distribuidor, pk=pk)
    return render(request, 'distribuidor/actualizar_distribuidor.html', {'distribuidor': distribuidor})


# [9] REALIZAR ACTUALIZACION DISTRIBUIDOR (POST - Guarda los cambios)
def realizar_actualizacion_distribuidor(request, pk):
    distribuidor = get_object_or_404(Distribuidor, pk=pk)
    
    if request.method == 'POST':
        try:
            distribuidor.nombre_distribuidor = request.POST.get('nombre_distribuidor')
            distribuidor.tipo_servicio = request.POST.get('tipo_servicio')
            distribuidor.ciudad = request.POST.get('ciudad')
            distribuidor.pais = request.POST.get('pais')
            distribuidor.tiempo_entrega_dias = request.POST.get('tiempo_entrega_dias')
            distribuidor.comision = request.POST.get('comision')
            
            distribuidor.save()
            return redirect('ver_distribuidores')
        except IntegrityError:
            contexto = {'error': 'Error: El Nombre del Distribuidor ya existe.', 'distribuidor': distribuidor}
            return render(request, 'distribuidor/actualizar_distribuidor.html', contexto)
    
    return redirect('ver_distribuidores') 


# [10] BORRAR DISTRIBUIDOR (GET/POST - Muestra confirmación/se utiliza como acción directa)
def borrar_distribuidor(request, pk):
    distribuidor = get_object_or_404(Distribuidor, pk=pk)
    
    if request.method == 'POST':
        distribuidor.delete()
        return redirect('ver_distribuidores')
        
    # Si es GET, muestra la página de confirmación
    return render(request, 'distribuidor/borrar_distribuidor.html', {'distribuidor': distribuidor})

# app_Proveedor/views.py (Fragmento, AÑADIR estas funciones)

# ... (Funciones CRUD para Distribuidor existentes)
# ...

# ----------------- Funciones para PRODUCTO -----------------

# [11] INICIO/VER PRODUCTO
def inicio_producto(request):
    """Muestra la lista de productos."""
    productos = Producto.objects.select_related('proveedor').all().order_by('nombre')
    return render(request, 'producto/ver_productos.html', {'productos': productos})

# [12] AGREGAR PRODUCTO (GET y POST)
def agregar_producto(request):
    proveedores = Proveedor.objects.all().order_by('nombre_empresa') 
    distribuidores = Distribuidor.objects.all().order_by('nombre_distribuidor') # Obtener lista de distribuidores

    contexto_base = {
        'proveedores': proveedores,
        'distribuidores': distribuidores 
    }
    
    if request.method == 'POST':
        # 1. Capturar todos los datos del formulario (incluyendo SKU)
        datos_formulario = {
            'nombre_producto': request.POST.get('nombre_producto'),
            'descripcion': request.POST.get('descripcion'),
            'precio': request.POST.get('precio'),
            'stock': request.POST.get('stock'),
            'proveedor_id': request.POST.get('proveedor_id'),
            'sku': request.POST.get('sku') 
        }
        proveedor_id = datos_formulario['proveedor_id'] 
        
        try:
            # 2. Obtener la instancia del proveedor y los IDs de distribuidores
            proveedor_instancia = Proveedor.objects.get(pk=proveedor_id)
            # request.POST.getlist se usa para campos 'multiple' de select
            distribuidores_ids = request.POST.getlist('distribuidores') 
            
            # 3. CREAR EL PRODUCTO y ASIGNARLO a 'nuevo_producto' (¡CORRECCIÓN CLAVE!)
            nuevo_producto = Producto.objects.create(
                nombre=datos_formulario['nombre_producto'],
                descripcion=datos_formulario['descripcion'],
                precio=datos_formulario['precio'],
                stock_actual=datos_formulario['stock'],
                sku=datos_formulario['sku'], 
                proveedor=proveedor_instancia 
            )
            
            # 4. Guardar la relación Muchos a Muchos (M2M)
            # Solo se puede llamar a .set() en el campo M2M después de que el objeto ha sido creado
            nuevo_producto.distribuidores.set(distribuidores_ids)
            
            return redirect('ver_productos')
        
        except IntegrityError:
            error_msg = 'Error: El Nombre del Producto o el SKU/Código ya existe.'
            contexto = {
                'error': error_msg, 
                'proveedores': proveedores,
                'distribuidores': distribuidores, # Persistencia de distribuidores
                'form_data': datos_formulario # Persistencia de campos llenados
            }
            return render(request, 'producto/agregar_producto.html', contexto)

        except Proveedor.DoesNotExist:
             error_msg = 'Error: El proveedor seleccionado no es válido.'
             contexto = {
                'error': error_msg, 
                'proveedores': proveedores,
                'distribuidores': distribuidores, 
                'form_data': datos_formulario 
            }
             return render(request, 'producto/agregar_producto.html', contexto)
    
    # Si es GET, simplemente renderiza el formulario
    return render(request, 'producto/agregar_producto.html', contexto_base)
        


# app_Proveedor/views.py (FUNCIÓN realizar_actualizacion_producto CORREGIDA)

# [13] ACTUALIZAR PRODUCTO (GET - Muestra el formulario con datos actuales)
def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    # Necesitas los proveedores y distribuidores para rellenar los select
    proveedores = Proveedor.objects.all().order_by('nombre_empresa')
    distribuidores = Distribuidor.objects.all().order_by('nombre_distribuidor')
    
    contexto = {
        'producto': producto, 
        'proveedores': proveedores,
        'distribuidores': distribuidores
    }
    return render(request, 'producto/actualizar_producto.html', contexto)

# [14] REALIZAR ACTUALIZACION PRODUCTO (POST - Guarda los cambios)
def realizar_actualizacion_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    # Obtener todas las listas necesarias para el contexto de error (GET)
    proveedores = Proveedor.objects.all().order_by('nombre_empresa') 
    distribuidores = Distribuidor.objects.all().order_by('nombre_distribuidor')
    
    if request.method == 'POST':
        
        # 1. Captura de datos para persistencia en caso de error
        datos_formulario = {
            'nombre_producto': request.POST.get('nombre_producto'),
            'descripcion': request.POST.get('descripcion'),
            'precio': request.POST.get('precio'),
            'stock': request.POST.get('stock'),
            'proveedor_id': request.POST.get('proveedor_id'),
            'sku': request.POST.get('sku'), # Capturar SKU
            'distribuidores': request.POST.getlist('distribuidores') # Capturar IDs de distribuidores M2M
        }
        
        proveedor_id = datos_formulario['proveedor_id']
        distribuidores_ids = datos_formulario['distribuidores'] # Lista de IDs seleccionados

        try:
            # 2. Obtener la instancia del Proveedor (objeto) usando el ID
            proveedor_instancia = Proveedor.objects.get(pk=proveedor_id)
            
            # 3. Actualizar campos (incluyendo SKU)
            producto.nombre = datos_formulario['nombre_producto']
            producto.descripcion = datos_formulario['descripcion']
            producto.precio = datos_formulario['precio']
            producto.stock_actual = datos_formulario['stock']
            producto.sku = datos_formulario['sku'] # 💥 ACTUALIZAR SKU
            producto.proveedor = proveedor_instancia 
            
            # Guardar en la BD el objeto principal
            producto.save()
            
            # 4. 💥 GUARDAR LA RELACIÓN MUCHOS A MUCHOS (M2M) 💥
            # .set() reemplaza las relaciones antiguas con las nuevas IDs
            producto.distribuidores.set(distribuidores_ids) 
            
            return redirect('ver_productos')
        
        except Proveedor.DoesNotExist:
            error_msg = 'Error: Proveedor no válido.'
            contexto = {'error': error_msg, 'producto': producto, 'proveedores': proveedores, 'distribuidores': distribuidores, 'form_data': datos_formulario}
            return render(request, 'producto/actualizar_producto.html', contexto)
            
        except IntegrityError:
            error_msg = 'Error: El Nombre o el SKU ya existe.'
            contexto = {'error': error_msg, 'producto': producto, 'proveedores': proveedores, 'distribuidores': distribuidores, 'form_data': datos_formulario}
            return render(request, 'producto/actualizar_producto.html', contexto)
    
    # Si no es POST o si el objeto no se encuentra, usamos el contexto simple
    contexto_get = {
        'producto': producto, 
        'proveedores': proveedores,
        'distribuidores': distribuidores
    }
    return render(request, 'producto/actualizar_producto.html', contexto_get)


# [15] BORRAR PRODUCTO (GET/POST)
def borrar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
        
    # Si es GET, muestra la página de confirmación
    return render(request, 'producto/borrar_producto.html', {'producto': producto})

# app_Proveedor/views.py

# ... (Tus funciones CRUD existentes para Proveedor, Distribuidor, Producto) ...

# ----------------- Funciones para EMPLEADO -----------------

# [16] VER/LISTAR EMPLEADOS
def ver_empleados(request):
    """Muestra la lista de todos los empleados."""
    # Nota: Asegúrate de que el modelo Empleado esté importado al inicio del archivo
    empleados = Empleado.objects.all().order_by('nombre')
    return render(request, 'empleado/ver_empleados.html', {'empleados': empleados})


# [17] AGREGAR EMPLEADO (GET y POST)
def agregar_empleado(request):
    """Muestra el formulario y procesa el POST para crear un nuevo empleado."""
    if request.method == 'POST':
        # Captura de datos del formulario POST
        datos_formulario = {
            'nombre': request.POST.get('nombre'),
            'puesto': request.POST.get('puesto'),
            'fecha_ingreso': request.POST.get('fecha_ingreso'),
            'salario': request.POST.get('salario'),
            'edad': request.POST.get('edad'),
        }

        try:
            # Validación básica: asegúrate de que todos los campos requeridos estén presentes
            if not all(datos_formulario.values()):
                raise ValueError("Todos los campos deben ser llenados.")
            
            # Crear el objeto Empleado en la base de datos
            Empleado.objects.create(
                nombre=datos_formulario['nombre'],
                puesto=datos_formulario['puesto'],
                fecha_ingreso=datos_formulario['fecha_ingreso'],
                salario=datos_formulario['salario'],
                edad=datos_formulario['edad'],
            )
            
            # Redirigir a la lista de empleados después de agregar
            return redirect('ver_empleados')
        
        except ValueError as e:
            # Manejo de error de validación
            error_msg = f"Error de Validación: {e}"
        except Exception as e:
            # Manejo de otros errores (p.ej., si Salario o Edad no son números válidos o formato de fecha incorrecto)
            error_msg = f"Error al guardar el empleado. Verifique que los campos numéricos y la fecha sean correctos. Detalle: {e}"
        
        # En caso de error, renderizar el formulario con el mensaje de error y los datos persistentes
        contexto = {
            'error': error_msg,
            'form_data': datos_formulario # Persistencia de los datos ingresados
        }
        return render(request, 'empleado/agregar_empleado.html', contexto)
    
    # Si es GET, simplemente renderiza el formulario vacío
    return render(request, 'empleado/agregar_empleado.html')


# [18] ACTUALIZAR EMPLEADO (GET - Muestra el formulario con datos actuales)
def actualizar_empleado(request, pk):
    """Muestra el formulario de edición para un empleado específico."""
    empleado = get_object_or_404(Empleado, pk=pk)
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})


# [19] REALIZAR ACTUALIZACION EMPLEADO (POST - Guarda los cambios)
def realizar_actualizacion_empleado(request, pk):
    """Procesa el POST para actualizar un empleado existente."""
    empleado = get_object_or_404(Empleado, pk=pk)
    
    if request.method == 'POST':
        datos_formulario = {
            'nombre': request.POST.get('nombre'),
            'puesto': request.POST.get('puesto'),
            'fecha_ingreso': request.POST.get('fecha_ingreso'),
            'salario': request.POST.get('salario'),
            'edad': request.POST.get('edad'),
        }

        try:
            if not all(datos_formulario.values()):
                raise ValueError("Todos los campos deben ser llenados.")
            
            # Actualizar campos
            empleado.nombre = datos_formulario['nombre']
            empleado.puesto = datos_formulario['puesto']
            empleado.fecha_ingreso = datos_formulario['fecha_ingreso']
            empleado.salario = datos_formulario['salario']
            empleado.edad = datos_formulario['edad']
            
            empleado.save()
            return redirect('ver_empleados')
            
        except ValueError as e:
            error_msg = f"Error de Validación: {e}"
        except Exception as e:
            error_msg = f"Error al actualizar el empleado. Verifique que los campos sean correctos. Detalle: {e}"
            
        # En caso de error, renderizar el formulario con error y datos persistentes
        contexto = {
            'error': error_msg,
            'empleado': empleado, # Mantener el objeto original para la URL de POST
            'form_data': datos_formulario # Persistencia de datos
        }
        return render(request, 'empleado/actualizar_empleado.html', contexto)
        
    return redirect('ver_empleados')


# [20] BORRAR EMPLEADO (GET/POST)
def borrar_empleado(request, pk):
    """Muestra confirmación o elimina un empleado específico."""
    empleado = get_object_or_404(Empleado, pk=pk)
    
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
        
    # Si es GET, muestra la página de confirmación
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})

# ----------------- Funciones para CLIENTE -----------------

# [21] VER/LISTAR CLIENTES
def ver_clientes(request):
    """Muestra la lista de todos los clientes."""
    clientes = Cliente.objects.all().order_by('nombre')
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

# [22] AGREGAR CLIENTE (GET y POST)
def agregar_cliente(request):
    """Muestra el formulario y procesa el POST para crear un nuevo cliente."""
    if request.method == 'POST':
        datos_formulario = {
            'nombre': request.POST.get('nombre'),
            'email': request.POST.get('email'),
            'telefono': request.POST.get('telefono'),
            'direccion': request.POST.get('direccion'),
            'pais': request.POST.get('pais'),
        }

        try:
            if not all(datos_formulario.values()):
                raise ValueError("Todos los campos deben ser llenados.")
            
            Cliente.objects.create(
                nombre=datos_formulario['nombre'],
                email=datos_formulario['email'],
                telefono=datos_formulario['telefono'],
                direccion=datos_formulario['direccion'],
                pais=datos_formulario['pais'],
            )
            
            return redirect('ver_clientes')
        
        except IntegrityError:
            error_msg = "Error: El email ya está registrado para otro cliente."
        except ValueError as e:
            error_msg = f"Error de Validación: {e}"
        except Exception as e:
            error_msg = f"Error al guardar el cliente. Detalle: {e}"
        
        contexto = {
            'error': error_msg,
            'form_data': datos_formulario
        }
        return render(request, 'cliente/agregar_cliente.html', contexto)
    
    return render(request, 'cliente/agregar_cliente.html')


# [23] ACTUALIZAR CLIENTE (GET - Muestra el formulario con datos actuales)
def actualizar_cliente(request, pk):
    """Muestra el formulario de edición para un cliente específico."""
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})


# [24] REALIZAR ACTUALIZACION CLIENTE (POST - Guarda los cambios)
def realizar_actualizacion_cliente(request, pk):
    """Procesa el POST para actualizar un cliente existente."""
    cliente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        datos_formulario = {
            'nombre': request.POST.get('nombre'),
            'email': request.POST.get('email'),
            'telefono': request.POST.get('telefono'),
            'direccion': request.POST.get('direccion'),
            'pais': request.POST.get('pais'),
        }

        try:
            if not all(datos_formulario.values()):
                raise ValueError("Todos los campos deben ser llenados.")
            
            # Actualizar campos
            cliente.nombre = datos_formulario['nombre']
            cliente.email = datos_formulario['email']
            cliente.telefono = datos_formulario['telefono']
            cliente.direccion = datos_formulario['direccion']
            cliente.pais = datos_formulario['pais']
            
            cliente.save()
            return redirect('ver_clientes')
            
        except IntegrityError:
            # Si el email ya existe en otro cliente
            error_msg = "Error: El email ya está registrado para otro cliente."
        except ValueError as e:
            error_msg = f"Error de Validación: {e}"
        except Exception as e:
            error_msg = f"Error al actualizar el cliente. Detalle: {e}"
            
        contexto = {
            'error': error_msg,
            'cliente': cliente,
            'form_data': datos_formulario
        }
        return render(request, 'cliente/actualizar_cliente.html', contexto)
        
    return redirect('ver_clientes')


# [25] BORRAR CLIENTE (GET/POST)
def borrar_cliente(request, pk):
    """Muestra confirmación o elimina un cliente específico."""
    cliente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
        
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# app_Proveedor/views.py (Funciones CRUD para Venta)

# ----------------- Funciones para VENTA -----------------

# [26] VER/LISTAR VENTAS
def ver_ventas(request):
    """Muestra la lista de todas las ventas."""
    ventas = Venta.objects.all().select_related('id_cliente', 'id_producto').order_by('-fecha_venta')
    return render(request, 'venta/ver_ventas.html', {'ventas': ventas})

# [27] AGREGAR VENTA (GET y POST)
def agregar_venta(request):
    """Muestra el formulario y procesa el POST para crear una nueva venta."""
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    
    if request.method == 'POST':
        datos_formulario = {
            'id_cliente': request.POST.get('id_cliente'),
            'id_producto': request.POST.get('id_producto'),
            'cantidad': request.POST.get('cantidad'),
            'costo_total': request.POST.get('costo_total'),
        }

        try:
            # Validación
            if not all(datos_formulario.values()):
                raise ValueError("Todos los campos deben ser llenados.")
            if int(datos_formulario['cantidad']) <= 0 or float(datos_formulario['costo_total']) <= 0:
                raise ValueError("Cantidad y Costo deben ser mayores a cero.")

            cliente = get_object_or_404(Cliente, pk=datos_formulario['id_cliente'])
            producto = get_object_or_404(Producto, pk=datos_formulario['id_producto'])
            
            Venta.objects.create(
                id_cliente=cliente,
                id_producto=producto,
                cantidad=datos_formulario['cantidad'],
                costo_total=datos_formulario['costo_total'],
                # fecha_venta se añade automáticamente
            )
            
            return redirect('ver_ventas')
        
        except ValueError as e:
            error_msg = f"Error de Validación: {e}"
        except Exception as e:
            error_msg = f"Error al guardar la venta. Verifique los campos. Detalle: {e}"
        
        contexto = {
            'error': error_msg,
            'form_data': datos_formulario,
            'clientes': clientes,
            'productos': productos,
        }
        return render(request, 'venta/agregar_venta.html', contexto)
    
    contexto = {
        'clientes': clientes,
        'productos': productos,
    }
    return render(request, 'venta/agregar_venta.html', contexto)

# [28] ACTUALIZAR VENTA (Muestra el formulario)
def actualizar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    contexto = {'venta': venta, 'clientes': clientes, 'productos': productos}
    return render(request, 'venta/actualizar_venta.html', contexto)

# [29] REALIZAR ACTUALIZACION VENTA (POST - Guarda los cambios)
def realizar_actualizacion_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    
    if request.method == 'POST':
        datos_formulario = {
            'id_cliente': request.POST.get('id_cliente'),
            'id_producto': request.POST.get('id_producto'),
            'cantidad': request.POST.get('cantidad'),
            'costo_total': request.POST.get('costo_total'),
        }

        try:
            if not all(datos_formulario.values()):
                raise ValueError("Todos los campos deben ser llenados.")

            venta.id_cliente = get_object_or_404(Cliente, pk=datos_formulario['id_cliente'])
            venta.id_producto = get_object_or_404(Producto, pk=datos_formulario['id_producto'])
            venta.cantidad = datos_formulario['cantidad']
            venta.costo_total = datos_formulario['costo_total']
            
            venta.save()
            return redirect('ver_ventas')
            
        except ValueError as e:
            error_msg = f"Error de Validación: {e}"
        except Exception as e:
            error_msg = f"Error al actualizar la venta. Detalle: {e}"
            
        contexto = {
            'error': error_msg,
            'venta': venta,
            'form_data': datos_formulario,
            'clientes': clientes,
            'productos': productos,
        }
        return render(request, 'venta/actualizar_venta.html', contexto)
        
    return redirect('ver_ventas')

# [30] BORRAR VENTA (GET/POST)
def borrar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('ver_ventas')
        
    return render(request, 'venta/borrar_venta.html', {'venta': venta})

# app_Proveedor/views.py (Funciones CRUD para Envío)

# ----------------- Funciones para ENVÍO -----------------

# [31] VER/LISTAR ENVÍOS
def ver_envios(request):
    """Muestra la lista de todos los envíos."""
    envios = Envio.objects.all().select_related('id_cliente').order_by('-fecha_envio')
    return render(request, 'envio/ver_envios.html', {'envios': envios})

# [32] AGREGAR ENVÍO (GET y POST)
def agregar_envio(request):
    """Muestra el formulario y procesa el POST para crear un nuevo envío."""
    clientes = Cliente.objects.all()
    
    if request.method == 'POST':
        datos_formulario = {
            'id_cliente': request.POST.get('id_cliente'),
            'estado': request.POST.get('estado'),
            'pais': request.POST.get('pais'),
            'direccion': request.POST.get('direccion'),
        }

        try:
            if not all(datos_formulario.values()):
                raise ValueError("Todos los campos deben ser llenados.")

            cliente = get_object_or_404(Cliente, pk=datos_formulario['id_cliente'])
            
            Envio.objects.create(
                id_cliente=cliente,
                estado=datos_formulario['estado'],
                pais=datos_formulario['pais'],
                direccion=datos_formulario['direccion'],
                # fecha_envio se añade automáticamente
            )
            
            return redirect('ver_envios')
        
        except ValueError as e:
            error_msg = f"Error de Validación: {e}"
        except Exception as e:
            error_msg = f"Error al guardar el envío. Detalle: {e}"
        
        contexto = {
            'error': error_msg,
            'form_data': datos_formulario,
            'clientes': clientes,
            'estados': Envio.estado.field.choices, # Pasa las opciones de CHOICES
        }
        return render(request, 'envio/agregar_envio.html', contexto)
    
    contexto = {
        'clientes': clientes,
        'estados': Envio.estado.field.choices, # Pasa las opciones de CHOICES
    }
    return render(request, 'envio/agregar_envio.html', contexto)

# [33] ACTUALIZAR ENVÍO (Muestra el formulario)
def actualizar_envio(request, pk):
    envio = get_object_or_404(Envio, pk=pk)
    clientes = Cliente.objects.all()
    contexto = {
        'envio': envio, 
        'clientes': clientes,
        'estados': Envio.estado.field.choices,
    }
    return render(request, 'envio/actualizar_envio.html', contexto)

# [34] REALIZAR ACTUALIZACION ENVÍO (POST - Guarda los cambios)
def realizar_actualizacion_envio(request, pk):
    envio = get_object_or_404(Envio, pk=pk)
    clientes = Cliente.objects.all()
    
    if request.method == 'POST':
        datos_formulario = {
            'id_cliente': request.POST.get('id_cliente'),
            'estado': request.POST.get('estado'),
            'pais': request.POST.get('pais'),
            'direccion': request.POST.get('direccion'),
        }

        try:
            if not all(datos_formulario.values()):
                raise ValueError("Todos los campos deben ser llenados.")

            envio.id_cliente = get_object_or_404(Cliente, pk=datos_formulario['id_cliente'])
            envio.estado = datos_formulario['estado']
            envio.pais = datos_formulario['pais']
            envio.direccion = datos_formulario['direccion']
            
            envio.save()
            return redirect('ver_envios')
            
        except ValueError as e:
            error_msg = f"Error de Validación: {e}"
        except Exception as e:
            error_msg = f"Error al actualizar el envío. Detalle: {e}"
            
        contexto = {
            'error': error_msg,
            'envio': envio,
            'form_data': datos_formulario,
            'clientes': clientes,
            'estados': Envio.estado.field.choices,
        }
        return render(request, 'envio/actualizar_envio.html', contexto)
        
    return redirect('ver_envios')

# [35] BORRAR ENVÍO (GET/POST)
def borrar_envio(request, pk):
    envio = get_object_or_404(Envio, pk=pk)
    if request.method == 'POST':
        envio.delete()
        return redirect('ver_envios')
        
    return render(request, 'envio/borrar_envio.html', {'envio': envio})