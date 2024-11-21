
from django.shortcuts import render, redirect
from .forms import PagoForm, ResidenteForm
from .models import Pago, Residente

def ingresar_residente(request):
    if request.method == 'POST':
        form = ResidenteForm(request.POST)
        if form.is_valid():
            residente = form.save()
            return redirect('ingresar_pago', residente_id=residente.id)
    else:
        form = ResidenteForm()
    return render(request, 'pagos/ingresar_residente.html', {'form': form})

def ingresar_pago(request, residente_id):
    residente = Residente.objects.get(id=residente_id)  # Obtener residente
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            pago = Pago(
                residente=residente,
                monto=form.cleaned_data['monto'],
                estado=True  # Simulamos que el pago es exitoso
            )
            pago.save()
            # Redirigir a pago_exitoso con nombre y apellido del residente
            return redirect('pago_exitoso', residente_id=residente.id)
    else:
        form = PagoForm()
    return render(request, 'pagos/ingresar_pago.html', {'form': form, 'residente': residente})

def pago_exitoso(request, residente_id):
    residente = Residente.objects.get(id=residente_id)  # Obtener residente de la base de datos
    return render(request, 'pagos/pago_exitoso.html', {'residente': residente})

