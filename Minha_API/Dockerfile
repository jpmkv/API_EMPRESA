# Define a imagem base que será utilizada
FROM python:3.9-slim-buster

# Define a variável de ambiente para evitar erros de codificação
ENV PYTHONUNBUFFERED=1

# Cria o diretório para a aplicação dentro do container
WORKDIR /Minha_API

# Copia os arquivos necessários para dentro do container
COPY requirements.txt /Minha_API/
COPY . /Minha_API/

# Instala as dependências da aplicação
RUN pip install -r requirements.txt

# Expõe a porta 8000
EXPOSE 8000

# Roda o comando para iniciar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
