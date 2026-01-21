from fastapi import APIRouter, HTTPException
import time
import hmac
import hashlib
from app.core.config import settings

router = APIRouter()

def generate_shopee_auth_url():
    if not all([settings.SHOPEE_PARTNER_ID, settings.SHOPEE_KEY, settings.SHOPEE_REDIRECT_URI]):
        return "https://shopee.com.br/affiliate"
        
    path = "/api/v2/shop/auth_partner"
    timestamp = int(time.time())
    base_string = f"{settings.SHOPEE_PARTNER_ID}{path}{timestamp}"
    sign = hmac.new(
        settings.SHOPEE_KEY.encode(), 
        base_string.encode(), 
        hashlib.sha256
    ).hexdigest()
    
    host = "https://partner.shopeemobile.com"
    return (
        f"{host}{path}"
        f"?partner_id={settings.SHOPEE_PARTNER_ID}"
        f"&timestamp={timestamp}"
        f"&sign={sign}"
        f"&redirect={settings.SHOPEE_REDIRECT_URI}"
    )

@router.get("/login")
async def login():
    """Gera a URL de login para conectar a conta Shopee"""
    try:
        auth_url = generate_shopee_auth_url()
        return {"url": auth_url}
    except Exception as e:
        return {"url": "https://shopee.com.br/affiliate"}

@router.get("/callback")
async def callback(code: str = None, shop_id: str = None):
    """Callback para processar o code retornado pela Shopee"""
    if not code:
        raise HTTPException(status_code=400, detail="Código não fornecido")
    
    return {
        "message": "Conexão Shopee iniciada", 
        "data": {
            "code": code, 
            "shop_id": shop_id, 
            "status": "pending_token_exchange"
        }
    }
