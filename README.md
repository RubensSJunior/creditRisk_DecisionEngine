# Credit Risk Decision Engine

## 📌 Visão Geral

Este projeto tem como objetivo construir um modelo de Machine Learning capaz de prever a **probabilidade de inadimplência (risco de crédito)** utilizando o dataset *Give Me Some Credit* do Kaggle.

O projeto segue a metodologia **SEMMA**:

* **Sample** – Seleção e divisão inicial dos dados
* **Explore** – Análise exploratória dos dados (EDA)
* **Modify** – Engenharia e tratamento das variáveis
* **Model** – Treinamento, ajuste e avaliação dos modelos
* **Assess** – (em desenvolvimento) Validação e análise de negócio

---

## 📂 Estrutura do Projeto

```text
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
│   ├── 04.02_model_xgboost.ipynb
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

## 🔍 Preparação dos Dados

### Explore

Nesta etapa foi realizada a análise exploratória dos dados com o objetivo de compreender o comportamento das variáveis e identificar possíveis problemas de qualidade dos dados.

Principais atividades:

* Análise da distribuição da variável alvo
* Avaliação da distribuição das variáveis numéricas
* Identificação de valores ausentes
* Investigação de possíveis outliers
* Avaliação inicial da relação entre variáveis e inadimplência

### Modify

Nesta etapa foi realizado o pré-processamento necessário para a modelagem.

Principais atividades:

* Tratamento de valores ausentes
* Criação e transformação de atributos
* Preparação dos dados para treinamento
* Separação dos conjuntos de treino e teste
* Exportação dos datasets processados para reutilização nas etapas de modelagem

---

## 🧠 Abordagem de Modelagem

### 🔹 Modelo Baseline

O modelo baseline foi desenvolvido utilizando **Regressão Logística**, servindo como referência inicial para comparação com modelos mais avançados.

Características:

* Regressão Logística
* Modelo de referência para benchmark
* Avaliação baseada em ROC-AUC
* Utilizado para medir os ganhos obtidos pelos modelos de Gradient Boosting

### 🔹 Modelos Avançados

#### 🌲 LightGBM

Modelo baseado em Gradient Boosting otimizado para eficiência computacional e desempenho em grandes volumes de dados.

Características:

* LightGBM Classifier
* Ajuste de hiperparâmetros com RandomizedSearchCV
* Validação cruzada estratificada
* Otimização baseada em ROC-AUC
* Comparação direta com o modelo baseline

#### ⚡ XGBoost

Modelo baseado em Gradient Boosting amplamente utilizado em problemas tabulares e competições de Machine Learning.

Características:

* XGBoost Classifier
* Ajuste de hiperparâmetros com RandomizedSearchCV
* Validação cruzada estratificada
* Otimização baseada em ROC-AUC
* Comparação direta com Baseline e LightGBM

---

## 📈 Estratégia de Avaliação

A avaliação dos modelos é realizada utilizando métricas adequadas para problemas de classificação binária desbalanceada.

### Métrica Principal

* **ROC-AUC**

### Análises Complementares

* ROC Curve
* Matriz de Confusão
* Classification Report
* Comparação de desempenho entre modelos

---

## 🧪 Monitoramento de Experimentos

O projeto utiliza o **MLflow** para rastreamento e auditoria dos experimentos.

### Estrutura

**Experimento**

```text
credit_default_modeling
```

**Runs**

* Baseline (Regressão Logística)
* LightGBM
* XGBoost

### Informações Registradas

* Hiperparâmetros dos modelos
* Métricas de avaliação
* Modelos treinados
* Artefatos gerados durante os experimentos

### Executar a Interface do MLflow

```bash
poetry run mlflow ui
```

Acesse em:

```text
http://localhost:5000
```

---

