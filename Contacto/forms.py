from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, max_length=50)
    email = forms.EmailField(label="Email", required=True, max_length=50)
    contenido = forms.CharField(label="Contenido", widget=forms.Textarea)