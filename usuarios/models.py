from django.db import models

# Create your models here.

class Usuario(models.Model):
    cpf = models.IntegerField(unique=True)
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
