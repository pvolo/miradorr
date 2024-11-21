
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
    residente = Residente.objects.get(id=residente_id)  
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            pago = Pago(
                residente=residente,
                monto=form.cleaned_data['monto'],
                estado=True  
            )
            pago.save()
            return redirect('pago_exitoso', residente_id=residente.id)
    else:
        form = PagoForm()
    return render(request, 'pagos/ingresar_pago.html', {'form': form, 'residente': residente})

def pago_exitoso(request, residente_id):
    residente = Residente.objects.get(id=residente_id)  
    return render(request, 'pagos/pago_exitoso.html', {'residente': residente})

