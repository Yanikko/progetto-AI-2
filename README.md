# Progetto AI 2 – Human Activity Recognition

Progetto per il corso di **Intelligenza Artificiale II**.  
Obiettivo: **classificare attività umane** a partire da dati di accelerometri indossabili, utilizzando modelli di machine learning classici con una pipeline metodologicamente corretta.

---

## Dataset

- **HARTH – Human Activity Recognition Trondheim**
- Fonte: **UCI Machine Learning Repository**
- Multivariate time-series
- 22 soggetti
- Accelerometri a **3 assi**
- Attività multiple con distribuzione non uniforme

Il dataset non è incluso nel repository per motivi di dimensione e viene scaricato automaticamente dai notebook.

---

## Struttura del repository
- `data/raw/`  
  Dati grezzi (non versionati)

- `notebooks/`
  - `01_eda_HARTH.ipynb` — analisi esplorativa sui dati raw  
  - `02_preprocessing_HARTH.ipynb` — preprocessing e feature engineering  
  - `03_modelli_HARTH.ipynb` — modelli e valutazione  
  - `04_run_all_HARTH.ipynb` — esecuzione completa della pipeline  

- `README.md`  
- `requirements.txt`

## Pipeline di lavoro

1. **EDA sui dati grezzi**  
   Analisi esplorativa per comprendere struttura del dataset, distribuzione delle classi e variabilità tra soggetti.

2. **Preprocessing & Feature Engineering**  
   - segmentazione temporale (windowing)
   - estrazione di feature nel dominio del tempo (mean, std)
   - creazione di un dataset compatto:
     - `X_features`
     - `y_labels`
     - `groups_subject`

3. **Modellazione e valutazione**
   - Logistic Regression (L2) come baseline
   - Linear Discriminant Analysis con shrinkage
   - split **per soggetto** per evitare data leakage
   - cross-validation solo sul training set
   - metriche: **macro-F1**, **balanced accuracy**, **confusion matrix**

---

## Aspetti metodologici
- Lo split per soggetto garantisce la **generalizzazione a persone non viste**
- Il preprocessing è **non supervisionato**
- La standardizzazione è eseguita **all’interno della pipeline**
- Il test set è utilizzato **una sola volta**
- **Nessun data leakage**

---

## Esecuzione

I notebook possono essere eseguiti singolarmente seguendo l’ordine numerico:

- `01_eda_HARTH.ipynb`

- `02_preprocessing_HARTH.ipynb`

- `03_modelli_HARTH.ipynb`

In alternativa, è possibile eseguire l’**intera pipeline** in sequenza aprendo ed eseguendo:

- `04_run_all_HARTH.ipynb`

---

## Requisiti

- Python ≥ 3.9
- Librerie elencate in `requirements.txt`

Installazione:

```bash
pip install -r requirements.txt




