from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class UsuarioView(View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        return render(request, 'usuario.html', {'usuarios': usuarios})

class EsporteView(View):
    def get(self, request, *args, **kwargs):
        esportes = Esporte.objects.all()
        return render(request, 'esporte.html', {'esportes': esportes})

class CategoriaEsportivaView(View):
    def get(self, request, *args, **kwargs):
        categorias = CategoriaEsportiva.objects.all()
        return render(request, 'categoriaesportiva.html', {'categorias': categorias})

class ExercicioView(View):
    def get(self, request, *args, **kwargs):
        exercicios = Exercicio.objects.all()
        return render(request, 'exercicio.html', {'exercicios': exercicios})

class LesaoView(View):
    def get(self, request, *args, **kwargs):
        lesoes = Lesao.objects.all()
        return render(request, 'lesao.html', {'lesoes': lesoes})

class TreinoView(View):
    def get(self, request, *args, **kwargs):
        treinos = Treino.objects.all()
        return render(request, 'treino.html', {'treinos': treinos})

class TreinoDiarioView(View):
    def get(self, request, *args, **kwargs):
        treinodiarios = TreinoDiario.objects.all()
        return render(request, 'treinodiario.html', {'treinodiarios': treinodiarios})

class FeedbackUsuarioView(View):
    def get(self, request, *args, **kwargs):
        feedbacks = FeedbackUsuario.objects.all()
        return render(request, 'feedbackusuario.html', {'feedbacks': feedbacks})

class RegistroFisicoView(View):
    def get(self, request, *args, **kwargs):
        registros = RegistroFisico.objects.all()
        return render(request, 'registrofisico.html', {'registros': registros})
