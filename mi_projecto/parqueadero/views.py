from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from .models import Parqueadero
from .forms import ParqueaderoForm, RegistroForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def lista_parqueaderos(request):
    parqueadero = Parqueadero.objects.all()
    print(type(parqueadero))
    return render(request, 'parqueadero/lista.html', {'parqueaderos': parqueadero})


def agregar_parquedero(request):
    if request.method == "POST":
        form = ParqueaderoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_parqueaderos')
    else:
        form = ParqueaderoForm()

    return render(request, 'parqueadero/agregar.html', {'form': form})


def editar_parqueadero(request, pk):
    parqueadero = get_object_or_404(Parqueadero, pk=pk)
    if request.method == "POST":
        form = ParqueaderoForm(request.POST, instance=parqueadero)
        if form.is_valid():
            form.save()
            # Redirige a la lista después de editar
            return redirect('lista_parqueaderos')
    else:
        form = ParqueaderoForm(instance=parqueadero)

    return render(request, 'parqueadero/editar_parqueadero.html', {'form': form, 'parqueadero': parqueadero})


def eliminar_parqueadero(request, pk):
    if request.method == "POST":
        parqueadero = get_object_or_404(Parqueadero, pk=pk)
        parqueadero.delete()
        return redirect('lista_parqueaderos')
    else:
        return HttpResponseNotAllowed(["POST"])


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Inicia sesion automaticamente despues del registro
            login(request, user)
            return redirect('lista_parqueadero')
    else:
        form = RegistroForm()

    return render(request, "registro.html", {"form", form})
