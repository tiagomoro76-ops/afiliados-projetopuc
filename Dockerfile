# 1️⃣ Escolher imagem base do Python
FROM python:3.11-slim

# 2️⃣ Definir diretório de trabalho no container
WORKDIR /app

# 3️⃣ Copiar todos os arquivos do projeto para dentro do container
COPY . /app

# 4️⃣ Atualizar pip e instalar pytest (para testes)
RUN pip install --upgrade pip
RUN pip install pytest

# 5️⃣ Comando padrão para rodar a aplicação
CMD ["python", "app.py"]
