from django.urls import path
from django.conf.urls.static import static

from projeto import settings
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.loginview, name='loginview'),
    path('index/', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('users/', views.exibir_user, name='exibir_user'),
    path('cursocadastro', views.cursos, name='cursos'),
    path('cursos', views.exibir_curso, name='exibir_curso'),
    path('editar_usuario/<int:id_usuario>', views.editar_usuario, name='editar_usuario'),
    path('excluir_usuario/<int:id_usuario>', views.excluir_usuario, name='excluir_usuario'),
    path('excluir_curso/<int:id_curso>', views.excluir_curso, name='excluir_curso'),
    path('excluir_foto/<int:id_foto>', views.excluir_foto, name='excluir_foto'),
    path('add-foto', views.add_foto, name='add_foto'),
    path('galeria', views.galeria, name='galeria'),
    path('compra/<int:id_curso>/', views.compra, name="CheckOut"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)