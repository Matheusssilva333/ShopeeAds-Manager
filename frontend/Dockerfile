# Use uma imagem oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Copia os requisitos
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Expõe a porta do Streamlit
EXPOSE 8501

# Healthcheck para garantir que o container está saudável
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Comando para rodar o Streamlit (usando $PORT do Render)
CMD sh -c "streamlit run streamlit_app.py --server.port=${PORT:-8501} --server.address=0.0.0.0"
