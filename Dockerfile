# Usar imagem oficial do Python
FROM python:3.11-slim

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar todos os arquivos do repositório para o container
COPY . .

# Instalar dependências se houver (requirements.txt)
# Se você não tiver, pode ignorar essa linha
RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar o app
CMD ["python", "app.py"]
