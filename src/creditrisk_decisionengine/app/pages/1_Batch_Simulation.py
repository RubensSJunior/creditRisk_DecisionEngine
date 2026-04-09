import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score,confusion_matrix
st.set_page_config(layout="wide")

st.title("Simulação de Crédito - Batch")

@st.cache_data
def load_data():
    X_test = pd.read_parquet("../../../data/final/X_test.parquet")
    y_test = pd.read_parquet("../../../data/final/y_test.parquet").values.ravel()
    preds  = pd.read_parquet("../../../data/final/preds.parquet").values.ravel()
    return X_test, y_test, preds

X_test, y_test, preds = load_data()


col1, col2, col3 = st.columns(3)

with col1:
    threshold = st.slider("Threshold", 0.0, 1.0, 0.4)

with col2:
    loan_value = st.number_input("Valor do empréstimo (R$)", value=1000)

with col3:
    lgd = st.slider("LGD (Loss Given Default)", 0.0, 1.0, 0.75)

approved = preds < threshold

cm = confusion_matrix(y_test, approved)

X_test["y_test"]   = y_test
X_test["approved"] = approved
X_test["approved"] = X_test["approved"].astype(int)

concedidos = X_test[X_test["approved"] == 0]
negados    = len(X_test[X_test["approved"] == 1])

naoPago = len(concedidos[concedidos["y_test"] == 1])
pago =    len(concedidos[concedidos["y_test"] == 0])

TP = cm[0][0]
TF = cm[0][1]
FP = cm[1][0]
FN = cm[1][1]




taxa = 0.022
n = 12

parcela = loan_value * (taxa * (1 + taxa)**n) / ((1 + taxa)**n - 1)
total_pago = parcela * n


totalInvestimento     = len(concedidos)*loan_value
totalEsperado  = len(concedidos)*total_pago
totalRecuperado       = pago*total_pago
totalNaoRecebido      = naoPago*loan_value


st.subheader("Visão Geral")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Clientes Aprovados", len(concedidos))
col2.metric("Clientes Negados"  , negados)
col3.metric("Clientes adimplentes", f"{pago}")
col4.metric("Clientes Inadimplentes", f"{naoPago}")

st.subheader("Comparação de Cenários")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Cenário ")

    st.metric("Total Gasto",        f"R$ {totalInvestimento:,.2f}")
    st.metric("Total Esperado",     f"R$ {totalEsperado:,.2f}")
    st.metric("Total Recebido",     f"R$ {totalRecuperado:,.2f}")
    st.metric("Total Não Recebido", f"R$ {totalNaoRecebido:,.2f}")
    

totalRetornoEsperado = totalEsperado - totalInvestimento
TotalRetornoObtido   = totalRecuperado - totalInvestimento

with col2:
    st.markdown("### Resultado")
    
    st.metric("Retorno Esperado", f"R$ {totalRetornoEsperado:,.2f}")
    st.metric("Resultado Obtido", f"R$ {TotalRetornoObtido:,.2f}")


    
    if TotalRetornoObtido >= 0:
        st.success(f"Resultado: R$ {TotalRetornoObtido:,.2f} (LUCRO)")
    else:
        st.error(f"Resultado: R$ {TotalRetornoObtido:,.2f} (PREJUÍZO)")

## ========================
## INSIGHT AUTOMÁTICO
## ========================
#st.subheader("🧠 Insight")
#
#impact = pred_result - real_result
#
#if impact > 0:
#    st.success(f"O modelo gerou um ganho adicional de R$ {impact:,.2f}")
#else:
#    st.error(f"O modelo gerou uma perda adicional de R$ {impact:,.2f}")