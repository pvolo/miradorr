from django.db import models

class Residente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_departamento = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} {self.apellido} - Departamento {self.numero_departamento}'

class Pago(models.Model):
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=False)  

    def __str__(self):
        return f'Pago de {self.residente.nombre} {self.residente.apellido} - Estado: {"Pagado" if self.estado else "Pendiente"}'

