import streamlit as st
import pandas as pd
import pickle
import shap
import numpy as np

st.set_page_config(layout="wide")

st.title("Simulação Individual de Crédito")

@st.cache_resource
def load_model():
    with open("../../../data/final/final_model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("../../../data/final/explainer.pkl", "rb") as f:
        explainer = pickle.load(f)

    return model, explainer

model, explainer = load_model()

st.subheader("Dados do cliente")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Idade", 18, 100, 35)
    monthly_income = st.number_input("Renda mensal", 0, 50000, 5000)

with col2:
    debt_ratio = st.slider("Debt Ratio", 0.0, 2.0, 0.5)
    credit_utilization = st.slider("Credit Utilization", 0.0, 1.0, 0.3)

with col3:
    late_30_59 = st.number_input("Atrasos 30-59 dias", 0, 20, 0)
    late_60_89 = st.number_input("Atrasos 60-89 dias", 0, 20, 0)
    late_90 = st.number_input("Atrasos 90+ dias", 0, 20, 0)

open_credit_lines = st.number_input("Linhas de crédito abertas", 0, 20, 5)
real_estate_loans = st.number_input("Empréstimos imobiliários", 0, 10, 1)
dependents = st.number_input("Dependentes", 0, 10, 0)

weighted_late = (
    late_30_59 +
    2 * late_60_89 +
    3 * late_90
)

input_df = pd.DataFrame([{
    "age": age,
    "monthly_income": monthly_income,
    "debt_ratio": debt_ratio,
    "credit_utilization": credit_utilization,
    "late_30_59_days": late_30_59,
    "late_60_89_days": late_60_89,
    "late_90_days": late_90,
    "open_credit_lines": open_credit_lines,
    "real_estate_loans": real_estate_loans,
    "dependents": dependents,
    'income_per_dependent': monthly_income/(dependents+1),
    "weighted_late": weighted_late
}])

threshold = st.slider("Threshold de decisão", 0.0, 1.0, 0.4)

pd_value = model.predict_proba(input_df)[:, 1][0]
decision = "APROVAR" if pd_value < threshold else "REJEITAR"

st.subheader("Resultado")

col1, col2 = st.columns(2)

col1.metric("Probabilidade de default (PD)", f"{pd_value:.2%}")

if decision == "APROVAR":
    col2.success("APROVADO")
else:
    col2.error("REJEITADO")


st.subheader("Explicação do modelo")
import matplotlib.pyplot as plt
shap_values = explainer(input_df)
fig, ax = plt.subplots()
shap.plots.waterfall(shap_values[0], show=False)
st.pyplot(fig)
plt.close(fig)


st.subheader("Principais fatores")

vals = shap_values.values[0]
features = input_df.columns

idx = np.argsort(np.abs(vals))[::-1][:3]

for i in idx:
    st.write(f"**{features[i]}** → impacto: {vals[i]:.3f}")