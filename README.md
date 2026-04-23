# End-to-End MLOps Projects Series

> A progressive series of production-grade ML pipelines — from raw data ingestion to deployed, monitored models.

## Projects Covered

| Project | Dataset | Algorithm | Status |
|---|---|---|---|
| Diabetes Prediction | Pima Indians | Logistic Regression / XGBoost | ✅ Deployed |
| Wine Quality | UCI Wine | Random Forest + MLflow tracking | ✅ Deployed |

## Pipeline Architecture

```
Raw Data (DVC versioned)
  → Data Ingestion
  → Data Validation (schema check)
  → Data Transformation
  → Model Training (scikit-learn)
  → Model Evaluation (MLflow)
  → Model Registry
  → Serving (FastAPI / Dagshub)
```

## Tech Stack

| Layer | Tool |
|---|---|
| Orchestration | Apache Airflow (Astronomer) |
| Experiment Tracking | MLflow |
| Data Versioning | DVC + DagHub |
| Containerization | Docker |
| ML Framework | Scikit-Learn |

## Quickstart

```bash
docker-compose up --build
# Airflow UI → http://localhost:8080
# MLflow UI  → http://localhost:5000
```

## Key Learnings

- Production pipeline design vs. notebook-style ML
- Reproducibility via DVC + MLflow artifact tracking
- Airflow DAG authoring for ML workflow orchestration

