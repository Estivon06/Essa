from django import forms
from django.contrib.auth import get_user_model
from .models import Queja, ComentarioQueja

Usuario = get_user_model()

# -------------------
# Formularios de PQR
# -------------------
class QuejaForm(forms.ModelForm):
    class Meta:
        model = Queja
        fields = ['ubicacion', 'tipo_falla', 'descripcion']

    def clean_descripcion(self):
        desc = self.cleaned_data['descripcion']
        if len(desc) < 10:
            raise forms.ValidationError("La descripción debe tener al menos 10 caracteres.")
        return desc


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = ComentarioQueja
        fields = ['mensaje']


class CambiarEstadoForm(forms.ModelForm):
    class Meta:
        model = Queja
        fields = ['estado']


# -------------------
# Formulario de Usuarios (para admin)
# -------------------
class UsuarioForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=False,
        help_text="Deja en blanco si no deseas cambiar la contraseña."
    )

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'rol', 'is_active', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        # Si se ingresó una nueva contraseña, la encripta
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
