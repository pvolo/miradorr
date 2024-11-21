from django.urls import path
from . import views

urlpatterns = [
    path('ingresar_residente/', views.ingresar_residente, name='ingresar_residente'),
    path('ingresar_pago/<int:residente_id>/', views.ingresar_pago, name='ingresar_pago'),
    path('pago_exitoso/<int:residente_id>/', views.pago_exitoso, name='pago_exitoso'),  
]
