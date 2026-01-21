import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .main {
            background-color: #f8f9fa;
        }
        
        /* Estilização dos Cards de Métrica */
        div[data-testid="stMetricValue"] {
            font-size: 1.8rem;
            font-weight: 700;
            color: #ff4b2b;
        }
        
        div[data-testid="stMetricDelta"] {
            font-size: 0.9rem;
        }

        .stButton>button {
            border-radius: 8px;
            background: linear-gradient(135deg, #ff4b2b 0%, #ff416c 100%);
            color: white;
            border: none;
            font-weight: 600;
            padding: 0.5rem 1rem;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            box-shadow: 0 4px 15px rgba(255, 75, 43, 0.3);
            transform: translateY(-1px);
        }

        /* Estilização da Sidebar */
        [data-testid="stSidebar"] {
            background-color: #ffffff;
            border-right: 1px solid #eee;
        }
        
        /* Glassmorphism Card */
        .glass-card {
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
        }
        </style>
        """, unsafe_allow_html=True)
