import pandas as pd
import io
from typing import List, Dict
from app.schemas.commission import CommissionRecord, CommissionSummary
from datetime import datetime

class CommissionService:
    @staticmethod
    async def process_file(file_content: bytes, filename: str) -> CommissionSummary:
        if filename.endswith('.csv'):
            df = pd.read_csv(io.BytesIO(file_content))
        elif filename.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(io.BytesIO(file_content))
        else:
            raise ValueError("Formato de arquivo não suportado. Use CSV ou Excel.")

        # Mapeamento de colunas típicas da Shopee (Afiliados Brasil)
        # Nota: As colunas podem variar, então usamos uma abordagem flexível
        column_mapping = {
            'ID do pedido': 'order_id',
            'Order ID': 'order_id',
            'Nome do produto': 'product_name',
            'Item Name': 'product_name',
            'Status do pedido': 'order_status',
            'Order Status': 'order_status',
            'Hora da conclusão do pedido': 'order_time',
            'Order Complete Time': 'order_time',
            'Valor do pagamento': 'checkout_amount',
            'Payout Amount': 'checkout_amount',
            'Comissão estimada': 'estimated_commission',
            'Estimated Commission': 'estimated_commission',
            'Taxa de comissão': 'commission_rate',
            'Commission Rate': 'commission_rate',
            'Tipo de conversão': 'conversion_type',
            'Conversion Type': 'conversion_type'
        }

        # Renomear as colunas encontradas
        df = df.rename(columns={c: column_mapping[c] for c in df.columns if c in column_mapping})

        # Preencher campos obrigatórios que podem faltar ou ter nomes diferentes
        required_cols = ['order_id', 'product_name', 'order_status', 'order_time', 'checkout_amount', 'estimated_commission']
        for col in required_cols:
            if col not in df.columns:
                # Se faltar, cria com valor padrão ou tenta inferir
                if col in ['checkout_amount', 'estimated_commission']:
                    df[col] = 0.0
                else:
                    df[col] = "N/A"

        # Limpeza e Conversão de Dados
        df['checkout_amount'] = pd.to_numeric(df['checkout_amount'].replace('[R$,]', '', regex=True), errors='coerce').fillna(0)
        df['estimated_commission'] = pd.to_numeric(df['estimated_commission'].replace('[R$,]', '', regex=True), errors='coerce').fillna(0)
        
        if 'commission_rate' not in df.columns:
            df['commission_rate'] = (df['estimated_commission'] / df['checkout_amount']).fillna(0)
        else:
             df['commission_rate'] = pd.to_numeric(df['commission_rate'].replace('[%,]', '', regex=True), errors='coerce').fillna(0)

        if 'conversion_type' not in df.columns:
            df['conversion_type'] = "Desconhecido"

        # Converter datas (Shopee usa diversos formatos)
        df['order_time'] = pd.to_datetime(df['order_time'], errors='coerce').fillna(datetime.now())

        records = []
        for _, row in df.iterrows():
            records.append(CommissionRecord(
                order_id=str(row['order_id']),
                product_name=str(row['product_name']),
                order_time=row['order_time'],
                order_status=str(row['order_status']),
                checkout_amount=float(row['checkout_amount']),
                estimated_commission=float(row['estimated_commission']),
                commission_rate=float(row['commission_rate']),
                conversion_type=str(row['conversion_type'])
            ))

        summary = CommissionSummary(
            total_orders=len(df),
            total_sales_value=df['checkout_amount'].sum(),
            total_estimated_commission=df['estimated_commission'].sum(),
            average_commission_rate=df['commission_rate'].mean() if len(df) > 0 else 0,
            records=records
        )

        return summary
