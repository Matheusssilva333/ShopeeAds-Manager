@echo off
echo ==========================================
echo    Iniciando ShopeeAds Manager (Docker)
echo ==========================================

if not exist "backend\.env" (
    echo [AVISO] Arquivo backend\.env nao encontrado!
    echo Copiando .env.example para .env...
    copy backend\.env.example backend\.env
)

docker-compose up --build
pause
