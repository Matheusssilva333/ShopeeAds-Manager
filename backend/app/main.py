from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import api_router
from app.core.config import settings
import os

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Backend para ShopeeAds Manager"
)

# Configuração CORS
origins = []
if settings.ALLOWED_ORIGINS:
    origins = [origin.strip() for origin in settings.ALLOWED_ORIGINS.split(",") if origin.strip()]

# Adicionar origem do ambiente (garantir que http esteja presente)
final_origins = []
for origin in origins:
    if not origin.startswith("http"):
        origin = f"https://{origin}"
    final_origins.append(origin)

app.add_middleware(
    CORSMiddleware,
    allow_origins=final_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Roteador Principal
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def read_root():
    return {
        "message": f"{settings.PROJECT_NAME} API está online 🚀",
        "status": "active",
        "version": settings.VERSION
    }

@app.get("/health")
async def health_check():
    return {"status": "ok"}
