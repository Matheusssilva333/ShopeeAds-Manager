import requests
import os
import streamlit as st

# Lógica de URL da API
API_URL = os.getenv("API_URL", "http://backend:8000")
if API_URL and not API_URL.startswith("http"):
    API_URL = f"https://{API_URL}"

API_V1_STR = "/api/v1"

def get_health():
    try:
        res = requests.get(f"{API_URL}/health", timeout=2)
        return res.status_code == 200
    except:
        return False

def get_metrics():
    try:
        res = requests.get(f"{API_URL}{API_V1_STR}/dashboard/metrics", timeout=2)
        if res.status_code == 200:
            return res.json()
    except:
        pass
    return None

def get_trends():
    try:
        res = requests.get(f"{API_URL}{API_V1_STR}/dashboard/trends", timeout=2)
        if res.status_code == 200:
            return res.json()
    except:
        pass
    return None

def get_auth_url():
    try:
        res = requests.get(f"{API_URL}{API_V1_STR}/auth/login", timeout=2)
        if res.status_code == 200:
            return res.json().get("url")
    except:
        pass
    return None
