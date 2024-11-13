from django import forms

class RegistroForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    correo = forms.EmailField(label='Correo')
    psw = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    psw2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
