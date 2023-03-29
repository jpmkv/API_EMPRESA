#criando o modelo de funcionário e migrando esse modelo para o banco de dados

from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=30)
    matricula = models.CharField(max_length=8)
    setor = models.CharField(max_length=30)
    salario = models.CharField(max_length=10)

    #método que serve para manipular os objetos dessa classe pelo nome, representação textual
    #ao invés do endereço de memória no computador, mas por um atributo da classe
    def __str__(self):
        return self.nome