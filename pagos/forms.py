from django import forms
from django.core.exceptions import ValidationError
from .models import Residente
import re



class ResidenteForm(forms.ModelForm):
    class Meta:
        model = Residente
        fields = ['nombre', 'apellido', 'numero_departamento']

        
class PagoForm(forms.Form):
    numero_tarjeta = forms.CharField(max_length=16)
    fecha_expiracion = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'MM/AA'}))
    titular = forms.CharField(max_length=100)
    codigo_seguridad = forms.CharField(max_length=3)
    monto = forms.DecimalField(max_digits=10, decimal_places=2)

    def clean_fecha_expiracion(self):
        fecha = self.cleaned_data['fecha_expiracion']
        if not re.match(r'^\d{2}/\d{2}$', fecha):
            raise ValidationError('Ingrese una fecha válida en formato MM/AA')
        return fecha


