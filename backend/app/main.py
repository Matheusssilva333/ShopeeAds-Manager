from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="DataVenda API",
    description="Backend para o SaaS de Análise de E-commerce Mercado Livre",
    version="1.0.0"
)

# Configuração CORS (Permitir que o frontend acesse a API)
origins = [
    "http://localhost:3000",  # Frontend Next.js
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.api import auth
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

@app.get("/")
async def read_root():
    return {
        "message": "DataVenda API está online 🚀",
        "status": "active",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    return {"status": "ok"}
