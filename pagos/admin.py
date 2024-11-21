from django.contrib import admin
from .models import Residente, Pago


@admin.register(Residente)
class ResidenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'numero_departamento')
    search_fields = ('nombre', 'apellido', 'numero_departamento')


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('residente', 'monto', 'fecha_pago', 'estado')
    list_filter = ('estado', 'fecha_pago')
    search_fields = ('residente__nombre', 'residente__apellido', 'residente__numero_departamento')
    list_editable = ('estado',)
