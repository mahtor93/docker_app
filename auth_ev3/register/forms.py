from django import forms

class RegistroForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=100)
    email = forms.EmailField(label='Correo electrónico', max_length=255)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        
        if password and password2 and password != password2:
            self.add_error('password2', 'Las contraseñas no coinciden.')
        
        return password2

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico', max_length=255)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
