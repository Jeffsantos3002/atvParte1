from django.urls import path
from . import views

urlpatterns = [
    path('usuario/', views.criar_usuario, name='criar_usuario'),
    path('usuario/<int:cpf>/', views.obter_usuario, name='obter_usuario'),
]
