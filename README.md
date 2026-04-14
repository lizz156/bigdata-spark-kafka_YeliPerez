# Análisis de datos con Spark y Kafka

## Descripción

En este proyecto se realiza el análisis de datos utilizando dos enfoques:

- Procesamiento por lotes (batch) con Apache Spark
- Procesamiento en tiempo real (streaming) con Apache Kafka y Spark Streaming

El objetivo es entender cómo se pueden procesar datos históricos y también datos en tiempo real simulando información de sensores.

---

## Entorno de trabajo

Todos los comandos fueron ejecutados en una máquina virtual previamente configurada con Hadoop y Apache Spark.

---

## Procesamiento por lotes (Batch)

Archivo:
```bash
- batch_analysis.py
```

Este script permite agrupar la información por sensor y calcular valores como el promedio.

### Ejecución

```bash
spark-submit batch_analysis.py
```

👩‍💻 Autor

Yeli Lizzeth pérez Sepúlveda
