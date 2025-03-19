from django import forms
from .models import Parqueadero
from django.contrib.auth.models import User


class ParqueaderoForm(forms.ModelForm):
    class Meta:
        model = Parqueadero
        fields = ['nombre', 'capacidad', 'ubicacion']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'capacidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la capacidad'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la ubicacion'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.strip():
            raise forms.ValidationError("El nombre no puede estar vacio.")
        return nombre

    def clean_capacidad(self):
        capacidad = self.cleaned_data.get('capacidad')
        if capacidad < 1:
            raise forms.ValidationError("La capacidad debe ser al menos 1.")
        return capacidad

    def clean_ubicacion(self):
        ubicacion = self.cleaned_data.get('ubicacion')
        if len(ubicacion) < 5:
            raise forms.ValidationError(
                "La ubicacion debe tener al menos 5 caracteres")
        return ubicacion


class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(
        widget=forms.PasswordInput, label="Confirmar Contraseña")

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        if self.changed_data['password'] != self.changed_data['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return self.cleaned_data['password2']
