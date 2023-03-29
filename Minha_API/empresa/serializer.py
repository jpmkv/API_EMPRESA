from rest_framework import serializers
from empresa.models import Funcionario

#serve para serializar o meu modelo criado para o banco de dados
class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'matricula', 'setor', 'salario']