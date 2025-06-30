from django.contrib import admin
from .models import (
    Usuario,
    Esporte,
    CategoriaEsportiva,
    Exercicio,
    Lesao,
    Treino,
    TreinoDiario,
    FeedbackUsuario,
    RegistroFisico,
    
)

admin.site.register(Usuario)
admin.site.register(Esporte)
admin.site.register(CategoriaEsportiva)
admin.site.register(Exercicio)
admin.site.register(Lesao)
admin.site.register(Treino)
admin.site.register(TreinoDiario)
admin.site.register(FeedbackUsuario)
admin.site.register(RegistroFisico)

