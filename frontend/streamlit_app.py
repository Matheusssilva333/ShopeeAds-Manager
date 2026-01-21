import streamlit as st
import pandas as pd
import plotly.express as px
from utils.api import get_health, get_metrics, get_trends, get_auth_url
from utils.styles import apply_custom_styles

# Configuração da página
st.set_page_config(
    page_title="ShopeeAds Manager | Dashboard",
    page_icon="🍊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Aplicar Estilos
apply_custom_styles()

# --- Sidebar ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Shopee-logo.svg/2560px-Shopee-logo.svg.png", width=120)
    st.title("Manager")
    st.markdown("---")
    page = st.sidebar.radio("Navegação", ["📈 Dashboard", "🔗 Integrações", "⚙️ Configurações"])
    
    st.markdown("---")
    st.markdown("### Status do Sistema")
    if get_health():
        st.success("API Online")
    else:
        st.warning("Conectando à API...")

# --- Dashboard Principal ---
if page == "📈 Dashboard":
    st.title("📈 Resumo de Performance")
    
    metrics = get_metrics()
    if metrics:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Receita Total (Mês)", f"R$ {metrics['revenue_total']:,.2f}", metrics['revenue_delta'])
        with col2:
            st.metric("Pedidos Totais", metrics['orders_total'], metrics['orders_delta'])
        with col3:
            st.metric("Comissão Estimada", f"R$ {metrics['commission_estimated']:,.2f}", metrics['commission_delta'])
        with col4:
            st.metric("Conversão", f"{metrics['conversion_rate']}%", metrics['conversion_delta'])
    else:
        st.info("Carregando métricas...")

    st.markdown("---")
    
    # Gráficos de Tendência
    trends = get_trends()
    if trends:
        col_left, col_right = st.columns([2, 1])
        
        with col_left:
            st.markdown("### 📊 Tendência de Vendas (7 dias)")
            sales_df = pd.DataFrame(trends['sales_trend'])
            fig = px.area(sales_df, x="date", y="value", line_shape="spline", 
                          color_discrete_sequence=['#ff4b2b'],
                          labels={"value": "Vendas (R$)", "date": "Data"})
            fig.update_layout(margin=dict(l=0, r=0, t=10, b=0), height=350)
            st.plotly_chart(fig, use_container_width=True)

        with col_right:
            st.markdown("### 🛒 Pedidos por Dia")
            orders_df = pd.DataFrame(trends['orders_trend'])
            fig2 = px.bar(orders_df, x="date", y="value", 
                          color_discrete_sequence=['#363636'],
                          labels={"value": "Quantidade", "date": "Data"})
            fig2.update_layout(margin=dict(l=0, r=0, t=10, b=0), height=350)
            st.plotly_chart(fig2, use_container_width=True)

elif page == "🔗 Integrações":
    st.header("🔗 Conectar Marketplace")
    st.info("Conecte sua conta de afiliado para automatizar a coleta de dados.")
    
    card_col = st.columns(3)[0]
    with card_col:
        st.markdown("""
            <div style="background: white; padding: 20px; border-radius: 15px; border: 1px solid #eee; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Shopee-logo.svg/2560px-Shopee-logo.svg.png" width="100">
                <h4 style="margin-top: 15px;">Shopee Affiliate</h4>
                <p style="color: #666; font-size: 0.9rem;">Sincronize pedidos, cliques e comissões automaticamente.</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("") # Espaçador
        if st.button("Conectar Shopee", use_container_width=True):
            auth_url = get_auth_url()
            if auth_url:
                st.link_button("Ir para Autenticação", auth_url)
            else:
                st.error("Serviço de autenticação indisponível.")

elif page == "⚙️ Configurações":
    st.header("⚙️ Configurações da Conta")
    
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.text_input("Nome da Loja", value="Minha Loja Afiliada")
        st.text_input("Email para Notificações", value="admin@exemplo.com")
        st.checkbox("Receber relatórios diários por email", value=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.write("")
    if st.button("Salvar Configurações"):
        st.success("Configurações salvas com sucesso!")
