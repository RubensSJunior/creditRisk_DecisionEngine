# 💳 Projeto de Credit Risk & Decision Engine

## 📌 Descrição do Projeto

Este projeto tem como objetivo construir um **motor de decisão de crédito (Credit Decision Engine)** utilizando técnicas de **Machine Learning** e **análise de risco**.

A aplicação permite:

* Estimar a **probabilidade de inadimplência (PD)** de clientes
* Simular decisões de concessão de crédito com base em diferentes **thresholds**
* Avaliar o impacto financeiro de estratégias de crédito
* Explicar decisões do modelo utilizando **SHAP (Explainability)**

Além disso, o projeto conta com uma interface interativa desenvolvida em **Streamlit**, com duas funcionalidades principais:

* 📊 **Simulação Batch**: análise de carteira de crédito e impacto financeiro
* 👤 **Simulação Individual**: avaliação de risco de um cliente específico

---

## ⚙️ Como instalar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/RubensSJunior/creditRisk_DecisionEngine
cd creditRisk_DecisionEngine
```

---

### 2. Ative o ambiente virtual

No Windows:

```bash
.\.venv\Scripts\activate
```

Ou, conforme o caminho informado:

```bash
creditRisk_DecisionEngine\.venv\Scripts\activate
```

---

### 3. Instale as dependências

Caso esteja utilizando Poetry:

```bash
poetry install
```

Ou, caso utilize pip:

```bash
pip install -r requirements.txt
```

---

## 🚀 Como executar a aplicação (Streamlit)

### 1. Navegue até a pasta do app

```bash
cd creditRisk_DecisionEngine\src\creditrisk_decisionengine\app
```

---

### 2. Execute o Streamlit

```bash
streamlit run Home.py
```

---

### 3. Acesse no navegador

Após executar o comando, a aplicação será aberta automaticamente no navegador.
Caso não abra, acesse manualmente:

```
http://localhost:8501
```

---

## 🧠 Observações

* Certifique-se de que os arquivos de modelo (`.pkl`) e dados estejam corretamente posicionados nos diretórios esperados.
* O projeto utiliza conceitos de:

  * Modelagem de risco de crédito
  * Engenharia de features
  * Avaliação com métricas (ROC AUC, Recall, Precision)
  * Simulação financeira com juros compostos
  * Explainability com SHAP

---

## 📌 Estrutura resumida

```
creditRisk_DecisionEngine/
│
├── .venv/
├── src/
│   └── creditrisk_decisionengine/
│       └── app/
│           ├── Home.py
│           ├── pages/
│
├── data/
├── model/
└── README.md
```

---

## ✅ Resultado

O projeto entrega um fluxo completo de:

* Modelagem de risco
* Tomada de decisão
* Avaliação financeira
* Interface interativa

Simulando de forma prática como sistemas de crédito são utilizados no mundo real.
