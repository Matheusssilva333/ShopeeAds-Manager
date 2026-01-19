from fastapi import APIRouter, HTTPException
import httpx
import os
import time
import hashlib
import hmac
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

# Configurações Shopee Open Platform
# Nota: A API de afiliados da Shopee muitas vezes requer aprovação específica ou uso de GraphQL em alguns casos.
# Esta implementação foca no fluxo padrão de OAuth2 da Shopee Open Platform.
SHOPEE_PARTNER_ID = os.getenv("SHOPEE_PARTNER_ID")
SHOPEE_KEY = os.getenv("SHOPEE_KEY")
SHOPEE_REDIRECT_URI = os.getenv("SHOPEE_REDIRECT_URI")
SHOPEE_HOST = "https://partner.shopeemobile.com" # Ou https://partner.test-stable.shopeemobile.com para sandbox

def generate_shopee_auth_url():
    # A lógica de assinatura da Shopee é complexa e baseada em HMAC-SHA256
    # Este é um placeholder para a geração da URL correta
    path = "/api/v2/shop/auth_partner"
    timestamp = int(time.time())
    base_string = f"{SHOPEE_PARTNER_ID}{path}{timestamp}"
    sign = hmac.new(SHOPEE_KEY.encode(), base_string.encode(), hashlib.sha256).hexdigest()
    
    return f"{SHOPEE_HOST}{path}?partner_id={SHOPEE_PARTNER_ID}&timestamp={timestamp}&sign={sign}&redirect={SHOPEE_REDIRECT_URI}"

@router.get("/login")
async def login():
    """Gera a URL de login para conectar a conta Shopee"""
    try:
        auth_url = generate_shopee_auth_url()
        return {"url": auth_url}
    except Exception as e:
        # Fallback simples se as credenciais não estiverem configuradas
        return {"url": "https://shopee.com.br/affiliate"}

@router.get("/callback")
async def callback(code: str, shop_id: str):
    """Callback para processar o code retornado pela Shopee"""
    if not code:
        raise HTTPException(status_code=400, detail="Código não fornecido")
    
    # Aqui implementaríamos a troca do code pelo access_token usando a assinatura correta
    # Devido à complexidade da assinatura da Shopee, simplificamos para este MVP
    
    return {
        "message": "Conexão Shopee iniciada", 
        "data": {"code": code, "shop_id": shop_id, "status": "pending_token_exchange"}
    }
