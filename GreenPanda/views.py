from django.shortcuts import render, redirect
from .models import RegistroP
from .forms import RegistrosForm

# Create your views here.

def Paginaprincipal(request):

    return render(request, 'Paginaprincipal.html'

      

    )

def Productos(request):

    return render(request, 'Productos.html'

      

    )

def QuienesSomos(request):

    return render(request, 'QuienesSomos.html'

      

    )

def Registro(request):

    return render(request, 'Registro.html'

      

    )

def Despacho(request):

    return render(request, 'Despacho.html'

      

    )

def Registros(request):

    registros = RegistroP.object.all

    return render(request, 'Registros.html', context ={ 'datos':registros},

      

    )


def form_registro(request):
    if request.method=='POST':
        registros_form = RegistrosForm(request.POST)
        if registros_form.is_valid():
            registros_form.save()
            return redirect('Registros')
    else:
        registros_form= RegistrosForm()
    return render(request, 'GreenPanda/form_registro.html', {'registro_form': registros_form}

      

    )

def form_mod_registros(request,id):
    registros = RegistrosForm.objects.get(NombreC=id)

    com ={
        'form': RegistrosForm(instance=registros)
    }
    if request.method=='POST':
        formulario = RegistrosForm(data=request.POST, instance = registros)
        if formulario.is_valid:
            formulario.save()
            return redirect('Registros')
    
    
    return render(request, 'GreenPanda/form_mod_registros.html', com
    
    
    
    )

def eliminar(request,id):
    registros = RegistrosForm.objects.get(NombreC=id)
    registros.delete()
    return redirect('Comentarios')