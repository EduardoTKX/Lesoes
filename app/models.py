from django.db import models

class Esporte(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    esporte = models.ForeignKey(Esporte, on_delete=models.CASCADE)
    tel = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome




class CategoriaEsportiva(models.Model):
    nome = models.CharField(max_length=100)
    faixa_etaria = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Exercicio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    esporte = models.ForeignKey(Esporte, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Lesao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_ocorrencia = models.DateField()
    esporte = models.ForeignKey(Esporte, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Lesão de {self.usuario.nome} em {self.data_ocorrencia}"


class Treino(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    esportes = models.ManyToManyField(Esporte)
    exercicios = models.ManyToManyField(Exercicio)

    def __str__(self):
        return self.nome


class TreinoDiario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)
    data = models.DateField()
    desempenho = models.TextField(blank=True)

    def __str__(self):
        return f"{self.usuario.nome} - {self.treino.nome} em {self.data}"


class FeedbackUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback de {self.usuario.nome}"


class RegistroFisico(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_registro = models.DateField()
    peso = models.FloatField(help_text="Peso em kg")
    altura = models.FloatField(help_text="Altura em metros")
   

    def save(self, *args, **kwargs):
        if self.altura > 0:
            self.imc = self.peso / (self.altura ** 2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Registro físico de {self.usuario.nome} - {self.data_registro}"

