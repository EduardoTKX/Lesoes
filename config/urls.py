"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('usuario/', UsuarioView.as_view(), name='usuario'),
    path('esporte/', EsporteView.as_view(), name='esporte'),
    path('categoriaesportiva/', CategoriaEsportivaView.as_view(), name='categoriaesportiva'),
    path('exercicio/', ExercicioView.as_view(), name='exercicio'),
    path('lesao/', LesaoView.as_view(), name='lesao'),
    path('treino/', TreinoView.as_view(), name='treino'),
    path('treinodiario/', TreinoDiarioView.as_view(), name='treinodiario'),
    path('feedbackusuario/', FeedbackUsuarioView.as_view(), name='feedbackusuario'),
    path('registrofisico/', RegistroFisicoView.as_view(), name='registrofisico'),
]

