from django.contrib import admin

#para utilizar o modelo de "funcionario" é preciso importa-lo
from empresa.models import Funcionario

#configuração de quais campos eu desejo visualizar em meus funcionários
class Funcionarios(admin.ModelAdmin):
    #campos eu desejo visualizar em meus funcionários
    list_display = ('id', 'nome', 'matricula', 'setor', 'salario')

    #campos que posso clicar para manipular os dados de funcionário
    list_display_links = ('id', 'nome')

    #campo pelo qual busco um funcionário
    search_fields = ('nome',)

#para visualizar um lista com as instâncias do modelo criado, no banco de dados.
admin.site.register(Funcionario, Funcionarios)