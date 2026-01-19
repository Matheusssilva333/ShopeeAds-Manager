import streamlit as st
import requests
import os

# Configuração da página
st.set_page_config(
    page_title="DataVenda - Análise de Vendas",
    page_icon="📊",
    layout="wide"
)

# Estilos CSS personalizados
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Título e Subtítulo
st.title("📊 DataVenda")
st.subheader("SaaS de Análise de Vendas e E-commerce")

# Sidebar
st.sidebar.title("Navegação")
page = st.sidebar.radio("Ir para", ["Dashboard", "Conectar Contas", "Configurações"])

API_URL = os.getenv("API_URL", "http://backend:8000")

if page == "Dashboard":
    st.info("Bem-vindo ao DataVenda. Conecte suas contas para ver os dados.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Vendas Hoje", value="R$ 0,00", delta="0%")
    with col2:
        st.metric(label="Pedidos", value="0", delta="0")
    with col3:
        st.metric(label="Ticket Médio", value="R$ 0,00", delta="0%")

    # Exemplo de chamada à API (Health Check)
    try:
        response = requests.get(f"{API_URL}/health")
        if response.status_code == 200:
            st.success("Backend conectado com sucesso!")
        else:
            st.warning("Backend respondeu com erro.")
    except Exception as e:
        st.error(f"Não foi possível conectar ao backend: {e}")

elif page == "Conectar Contas":
    st.header("Integrações")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Shopee-logo.svg/2560px-Shopee-logo.svg.png", width=150)
        if st.button("Conectar Shopee"):
            try:
                # Chama o backend para pegar a URL de auth
                res = requests.get(f"{API_URL}/api/auth/login")
                if res.status_code == 200:
                    auth_url = res.json().get("url")
                    st.link_button("Ir para Login Shopee", auth_url)
                else:
                    st.error("Erro ao obter URL de autenticação")
            except Exception as e:
                st.error(f"Erro de conexão: {e}")

    with col2:
        st.write("Outras integrações em breve...")

elif page == "Configurações":
    st.write("Configurações do sistema")
