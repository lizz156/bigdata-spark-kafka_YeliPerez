# Análisis de datos con Spark y Kafka

## 📌 Descripción

En este proyecto se realiza el análisis de datos utilizando dos enfoques:

- Procesamiento por lotes (batch) con Apache Spark
- Procesamiento en tiempo real (streaming) con Apache Kafka y Spark Streaming

El objetivo es entender cómo se pueden procesar datos históricos y también datos en tiempo real simulando información de sensores.

---

## 📊 Procesamiento por lotes (Batch)

Para esta parte se utilizó Spark con el fin de analizar datos y obtener resultados agregados.

Archivo utilizado:
- batch_analysis.py

Este script permite agrupar la información por sensor y calcular valores como el promedio.

### ▶️ Ejecución

```bash
spark-submit batch_analysis.py
