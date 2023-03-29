from rest_framework import viewsets

#modelo utillizado
from empresa.models import Funcionario

#serializador utilizado
from empresa.serializer import FuncionarioSerializer

from rest_framework.response import Response
from rest_framework import status

class FuncionariosViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all() #trazer todos os funcionários
    serializer_class = FuncionarioSerializer #classe serializadora reponsável por FuncionariosViewSet

    #post
    def create(self, request, *args, **kwargs):
        # Obter o cabeçalho personalizado a ser adicionado
        custom_header = "cabecalho_post_personalizado"
        custom_header_value = "funcionario criado"

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Verificar se o Funcionario já existe na base de dados
        funcionario_exists = Funcionario.objects.filter(matricula=serializer.validated_data['matricula']).exists()

        # Caso o Funcionario já exista na base de dados, retornar um erro de conflito
        if funcionario_exists:
            return Response({'error': 'Funcionario já existe na base de dados.'}, status=status.HTTP_409_CONFLICT)

        # Salvar o novo Funcionario na base de dados
        self.perform_create(serializer)


        # Adicionar o cabeçalho personalizado na resposta POST
        headers = self.get_success_headers(serializer.data)
        headers.update({custom_header: custom_header_value})
 
        # Caso contrário, retornar 201 CREATED
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    #delete
    def destroy(self, request, *args, **kwargs):
        # Obter o cabeçalho personalizado a ser adicionado
        custom_header = "cabecalho_delete_personalizado"
        custom_header_value = "funcionario deletado"

        # Executar o método padrão destroy do DRF
        instance = self.get_object()
        self.perform_destroy(instance)

        # Criar a resposta com o cabeçalho personalizado adicionado
        headers = {custom_header: custom_header_value}
    
        return Response(status=status.HTTP_204_NO_CONTENT, headers=headers)
    
    #put
    def update(self, request, *args, **kwargs):
        # Obter o cabeçalho personalizado a ser adicionado
        custom_header = "cabecalho_put_personalizado"
        custom_header_value = "dados do funcionario atualizado"

        # Executar o método padrão update do DRF
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Criar a resposta com o cabeçalho personalizado adicionado
        headers = {custom_header: custom_header_value}
        return Response(serializer.data, headers=headers)
    