from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import  RegistroP


class RegistrosForm(forms.ModelForm):

    class Meta:
        model= RegistroP
        fields = ['NumeroId', 'fotoLogoP', 'NombreC','Telefono','Direccion','Email','Pais','MonedaPago']
        labels ={
            'NumeroId': 'Numero de identificacion',
            'fotoLogoP': 'Fotografia/Logo que identifique al proveedor',
            'NombreC': 'Nombre Completo',
            'Telefono': 'Numero telefonico',
            'Direccion': 'Direccion',
            'Email': 'Email',
            'Pais': 'Pais',
            'MonedaPago': 'Moneda de pago',



        }
        widgets={
            'NumeroId': forms.IntegerField(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Numero de identificacion', 
                    'id': 'numeroid'
                }
            ),
            
            'NombreC': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ),
            'Telefono': forms.IntegerField(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Numero telefonico', 
                    'id': 'numero'
                }
            ),
            'Direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese direccion', 
                    'id': 'direccion',
                     
                }
            ),
            'Email': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese email', 
                    'id': 'email',
                     
                }
            ),
            'Pais': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese direccion', 
                    'id': 'direccion',
                     
                }
            ),
            'MonedaPago': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Moneda de pago', 
                    'id': 'monedapago',
                     
                }
            )
        }