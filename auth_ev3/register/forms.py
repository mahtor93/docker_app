from django import forms

class RegistroForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    correo = forms.EmailField(label='Correo')
    psw = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    psw2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    def clean_psw2(self):
        psw = self.cleaned_data.get('psw')
        psw2 = self.cleaned_data.get('psw2')
        
        if psw and psw2 and psw != psw2:
            self.add_error('psw2','Las contraseñas no coinciden.')
            
        return psw2
    
class LoginForm(forms.Form):
    correo = forms.EmailField(label='Correo')
    psw = forms.CharField(label='Contraseña', widget=forms.PasswordInput)