from datetime import timedelta
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from . import forms
from . import models

# Create your views here.

def index(request):
    email_do_usuario = request.session.get('email')
    context = {
        'email_do_usuario': email_do_usuario,
    }
    return render(request, 'app/index.html', context)

def cursos(request):
    new_curso = forms.CursoForm(request.POST or None, request.FILES or None)
    if request.POST:
        if new_curso.is_valid():
            new_curso.save()
            messages.success(request, "Curso cadastrado")
            return redirect('app:index')
    return render(request, 'app/add_curso.html', {'form': new_curso})

def signup(request):
    new_user = forms.UserForm(request.POST or None)
    if request.POST:
        if new_user.is_valid():
              new_user.save()
              messages.success(request, "Usuario Cadastrado com Sucesso!")
              return redirect('app:index')
    return render(request, 'app/signup.html', {'form': new_user})

def exibir_user(request):
    users = models.User.objects.all().values()
    context = {
          'dados' : users
     }
    return render (request, 'app/user.html', context)

def exibir_curso(request):
    curso = models.Curso.objects.all().values()
    context = {
          'dados' : curso
     }
    return render (request, 'app/curso.html', context)

def loginview(request):
    formL = forms.FormLogin(request.POST or None)
    if request.method == 'POST':
        return redirect('app:index') 

    context = {
        'formLogin': formL
    }
    return render(request, 'app/login.html', context)

def editar_usuario(request, id_usuario):
    usuario = models.User.objects.get(id=id_usuario)
    form = forms.UserForm(request.POST or None, instance=usuario)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('app:index')
    context = {
        'form' : form
    }
    return render(request, 'app/editar_usuario.html', context)

def excluir_usuario(request, id_usuario):
    usuario = models.User.objects.get(id=id_usuario)
    usuario.delete()
    return redirect('app:index')

def add_foto(request):
    if request.method == 'POST':
        form = forms.FormFoto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        form = forms.FormFoto()
    return render(request, 'app/fotos.html',{'form':form})
    
def galeria(request):
    fotos = models.foto.objects.all().values()

    context = {
        'galeria' :fotos
    }
    return render(request, 'app/galeria.html', context)

def excluir_curso(request, id_curso):
    curso = models.Curso.objects.get(id=id_curso)
    curso.delete()
    return redirect('app:index')

def excluir_foto(request, id_foto):
    foto = models.foto.objects.get(id=id_foto)
    foto.delete()
    return redirect('app:index')

def compra(request, id_curso):
    curso = get_object_or_404(models.Curso, id=id_curso)
    if request.method == 'POST':
        messages.success(request, "Compra Realizada com Sucesso!")
        return redirect('app:index')
    return render(request, 'app/compra.html', {'curso': curso})
