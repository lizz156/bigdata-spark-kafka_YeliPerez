# Análisis de Datos con Spark y Kafka

## Descripción
Este proyecto implementa análisis de datos en batch utilizando Apache Spark y procesamiento en tiempo real utilizando Kafka y Spark Streaming.

## Procesamiento Batch
Se realiza análisis de datos históricos con Spark para obtener métricas agregadas.

## Procesamiento en Tiempo Real
Se implementa un sistema de streaming donde:
- Un productor genera datos de sensores
- Kafka transmite los datos
- Spark Streaming procesa la información en tiempo real

## Ejecución

### 1. Iniciar servicios
```bash
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties
