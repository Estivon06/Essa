from django import forms
from django.contrib.auth import get_user_model
from .models import Queja, ComentarioQueja, Ciudadano

Usuario = get_user_model()

class QuejaForm(forms.ModelForm):
    class Meta:
        model = Queja
        fields = ['ubicacion', 'tipo_falla', 'descripcion']
        widgets = {
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_falla': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'ubicacion': 'Ubicación',
            'tipo_falla': 'Tipo de falla',
            'descripcion': 'Descripción',
        }

    def clean_descripcion(self):
        desc = self.cleaned_data.get('descripcion', '')
        if len(desc) < 10:
            raise forms.ValidationError("La descripción debe tener al menos 10 caracteres.")
        return desc


class QuejaFormAdmin(forms.ModelForm):
    class Meta:
        model = Queja
        fields = ['ciudadano', 'ubicacion', 'tipo_falla', 'descripcion']
        widgets = {
            'ciudadano': forms.Select(attrs={'class': 'form-select'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_falla': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'ciudadano': 'Ciudadano',
            'ubicacion': 'Ubicación',
            'tipo_falla': 'Tipo de falla',
            'descripcion': 'Descripción',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ordenar y mostrar una lista clara de ciudadanos
        self.fields['ciudadano'].queryset = Ciudadano.objects.select_related('usuario').order_by('usuario__username')
        # Opcional: mostrar un label más legible en el select si tu modelo Ciudadano define __str__
        # Si quieres personalizar opciones, puedes construir choices manualmente aquí.


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = ComentarioQueja
        fields = ['mensaje']
        widgets = {
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escribe tu comentario...'}),
        }
        labels = {
            'mensaje': 'Comentario',
        }

    def clean_mensaje(self):
        msg = self.cleaned_data.get('mensaje', '')
        if not msg.strip():
            raise forms.ValidationError("El mensaje no puede estar vacío.")
        return msg


class CambiarEstadoForm(forms.ModelForm):
    class Meta:
        model = Queja
        fields = ['estado']
        widgets = {
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'estado': 'Estado',
        }


# Opcional: formulario de usuario si lo necesitas aquí (creación/edición desde admin personalizado)
from django.contrib.auth import password_validation

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False,
        help_text="Deja en blanco si no deseas cambiar la contraseña."
    )

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'rol', 'is_active', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'rol': forms.Select(attrs={'class': 'form-select'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'username': 'Usuario',
            'email': 'Correo electrónico',
            'rol': 'Rol',
            'is_active': 'Activo',
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        if pwd:
            password_validation.validate_password(pwd, self.instance)
        return pwd

    def save(self, commit=True):
        user = super().save(commit=False)
        pwd = self.cleaned_data.get('password')
        if pwd:
            user.set_password(pwd)
        if commit:
            user.save()
        return user
