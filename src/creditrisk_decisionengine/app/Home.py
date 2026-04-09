import streamlit as st

st.set_page_config(page_title="Credit Risk Simulator", layout="wide")

st.title("💳 Credit Risk Simulator")

st.markdown("""
Bem-vindo ao simulador de crédito.

Use o menu lateral para navegar entre:

- 📊 Simulação Batch (carteira)
- 👤 Simulação Individual (cliente)

Este projeto demonstra:
- Modelagem de risco de crédito
- Otimização de threshold
- Impacto financeiro
- Explainability com SHAP
""")