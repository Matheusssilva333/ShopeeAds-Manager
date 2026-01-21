# 🍊 ShopeeAds Manager - SaaS para Afiliados

A plataforma definitiva e profissional para gestão de comissões, vendas e anúncios para afiliados da Shopee. Construída com uma arquitetura moderna em **Python**, **FastAPI** e **Streamlit**.

## 🚀 Funcionalidades Principais

- **📊 Dashboard Analytics**: Visualização profissional de métricas, tendências de vendas e conversão.
- **🔗 Automação Shopee**: Integração direta com a Shopee Open Platform (OAuth 2.0).
- **📉 Gestão de Performance**: Acompanhamento de pedidos, cliques e previsões de comissão.
- **🐳 Docker Ready**: Ambiente totalmente containerizado para desenvolvimento e produção.

## 📁 Estrutura do Projeto

```text
├── backend/            # API FastAPI (Pydantic v2, Clean Architecture)
│   ├── app/
│   │   ├── api/        # Endpoints v1 modularizados
│   │   ├── core/       # Configurações e segurança
│   │   ├── services/   # Lógica de integração externa
│   └── Dockerfile
├── frontend/           # Interface Streamlit Premium
│   ├── utils/          # API calls e estilização
│   ├── streamlit_app.py
│   └── Dockerfile
└── docker-compose.yml  # Orquestração local
```

## 🛠️ Configuração e Instalação

### Pré-requisitos
- Docker & Docker Compose instalados.

### Rodando o Projeto

1.  **Windows**: Basta clicar duas vezes no arquivo `start.bat`.
2.  **Terminal**: 
    ```bash
    docker-compose up --build
    ```

### Acesso rápido:
- **Painel Web**: [http://localhost:8501](http://localhost:8501)
- **Documentação API**: [http://localhost:8000/docs](http://localhost:8000/docs)

## ☁️ Deploy no Render

Este projeto já está configurado para o Render via Blueprint (`render.yaml`).
1. Conecte seu GitHub no Render.com.
2. Selecione **New > Blueprint Instance**.
3. O Render configurará automaticamente o Frontend e Backend como serviços Docker.

---
Desenvolvido com foco em alta performance e design premium.