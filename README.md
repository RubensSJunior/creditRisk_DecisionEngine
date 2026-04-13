# Credit Risk Decision Engine

## 📌 Visão Geral

Este projeto tem como objetivo construir um modelo de Machine Learning capaz de prever a **probabilidade de inadimplência (risco de crédito)** utilizando o dataset *Give Me Some Credit* do Kaggle.

O projeto segue a metodologia **SEMMA**:

* **Sample** – Seleção e divisão inicial dos dados
* **Explore** – Análise exploratória (EDA)
* **Modify** – Engenharia e tratamento de variáveis
* **Model** – Treinamento, ajuste e avaliação dos modelos
* **Assess** – (em desenvolvimento) Validação e análise de negócio

---

## 📂 Estrutura do Projeto

```
.
├── .gitattributes
├── .gitignore
├── .python-version
├── README.md
├── data
│   ├── final
│   ├── processed
│   │   ├── X_test.parquet
│   │   ├── X_train.parquet
│   │   ├── test_data.csv
│   │   ├── train_data.csv
│   │   ├── y_test.parquet
│   │   └── y_train.parquet
│   └── raw
│       ├── Data Dictionary.xls
│       ├── cs-test.csv
│       ├── cs-training.csv
│       └── sampleEntry.csv
├── mlflow.db
├── notebook
│   ├── 01_sample.ipynb
│   ├── 02_explore.ipynb
│   ├── 03_modify.ipynb
│   ├── 04.00_model_baseline.ipynb
│   ├── 04.01_model_lgbm.ipynb
│   ├── 04.02_model_deepLearning.ipynb
│   └── 05_assess.ipynb
├── poetry.lock
├── pyproject.toml
├── src
│   └── creditrisk_decisionengine
│       ├── __init__.py
│       └── app
│           ├── Home.py
│           └── pages
│               ├── 1_Batch_Simulation.py
│               └── 2_Individual_Simulation.py
└── tests
    └── __init__.py
```

---

## ⚙️ Ambiente

O projeto utiliza o **Poetry** para gerenciamento de dependências.

### Instalar dependências

```bash
poetry install
```

### Ativar ambiente

```bash
poetry shell
```

---

## 📊 Dataset

* Fonte: Kaggle – *Give Me Some Credit*
* Tipo: Classificação binária
* Target: Inadimplente (1) vs Não inadimplente (0)

---

## 🧠 Abordagem de Modelagem

### 🔹 Modelo Baseline

* Regressão Logística
* Tratamento de desbalanceamento com `class_weight='balanced'`

### 🔹 Modelos Avançados

#### 🌲 LightGBM + RandomizedSearchCV

* Busca aleatória de hiperparâmetros
* Validação cruzada estratificada
* Otimização baseada em ROC-AUC

#### ⚡ LightGBM + Optuna

* Otimização Bayesiana
* Exploração mais eficiente do espaço de busca
* Foco em maximizar ROC-AUC

---

## 📈 Estratégia de Avaliação

* Métrica principal: **ROC-AUC**
* Análises complementares:

  * Matriz de confusão
  * Classification report
  * Ajuste de threshold

---

## 🧪 Monitoramento de Experimentos

O projeto utiliza o **MLflow** para rastreamento e auditoria dos modelos.

### Estrutura

* **Experimento:** `credit_default_modeling`
* **Runs:**

  * Baseline (Regressão Logística)
  * LightGBM (Random Search)
  * LightGBM (Optuna)

### Informações registradas

* Parâmetros (hiperparâmetros)
* Métricas (ROC-AUC)
* Artefatos (modelos treinados, gráficos, etc.)

### Executar a interface do MLflow

```bash
poetry run mlflow ui
```

Acesse em:

```
http://localhost:5000
```

## 👤 Autor

Rubens dos Santos Junior