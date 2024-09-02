from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=14, unique=True)
    domicilio = models.CharField(max_length=50)
    telefono = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} {self.telefono} {self.email}"


class Producto(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    categoria = models.CharField(max_length=150)
    tipo = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    unidad = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    img = models.CharField(max_length=500)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.marca} {self.precio} {self.descripcion}"


class Pedido(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        EN_PROCESO = 'EN_PROCESO', 'En proceso'
        ENVIADO = 'ENVIADO', 'Enviado'
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=15, choices=Estado.choices, default=Estado.PENDIENTE)

    def __str__(self) -> str:
        return f"Pedido del cliente {self.cliente.nombre}, {self.producto.nombre}"