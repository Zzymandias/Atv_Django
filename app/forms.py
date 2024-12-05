from django import forms
from . import models
from app.models import Login, foto

class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('name', 'email', 'hash_senha')
        widgets = {
            'name': forms.TextInput(),
            'email': forms.EmailInput(),
            'hash_senha': forms.PasswordInput()
        }


class CursoForm(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields = ('name', 'author', 'duration', 'price', 'fotos')
        widgets = {
            'name': forms.TextInput(),
            'author': forms.TextInput(),
            'duration': forms.NumberInput(),
            'price': forms.NumberInput(),
            'fotos': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class FormLogin(forms.ModelForm): 
    class Meta:
        model = models.Login
        fields = ("email","senha")
        
        widgets = {
            'email' : forms.TextInput(attrs={'class': 'form-control border border-sucess', 'type': 'email'}),
            'senha' : forms.TextInput(attrs={'class': 'form-control border border-sucess', 'type': 'password'})
        }
            
class FormFoto (forms.ModelForm):
    class Meta:
        model = foto
        fields = ['nome', 'foto']
        
        widgets = {
            'foto': forms.FileInput(attrs={'accept':'image/'})
        }
