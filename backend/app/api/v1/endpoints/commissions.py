from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.commission_service import CommissionService
from app.schemas.commission import CommissionSummary

router = APIRouter()

@router.post("/upload", response_model=CommissionSummary)
async def upload_commissions(file: UploadFile = File(...)):
    """
    Exporta e processa planilha de comissões da Shopee.
    Aceita arquivos .csv, .xlsx e .xls.
    """
    if not file.filename.endswith(('.csv', '.xlsx', '.xls')):
        raise HTTPException(status_code=400, detail="Formato de arquivo inválido. Envie um CSV ou Excel.")
    
    try:
        content = await file.read()
        summary = await CommissionService.process_file(content, file.filename)
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar arquivo: {str(e)}")
