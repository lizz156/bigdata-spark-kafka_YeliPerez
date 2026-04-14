# Análisis de Datos en Batch y Streaming con Spark y Kafka

## Descripción
Este proyecto implementa el análisis de datos en batch utilizando Apache Spark, y procesamiento en tiempo real utilizando Apache Kafka y Spark Streaming.

## Tecnologías utilizadas
- Apache Spark
- Apache Kafka
- Python
- Hadoop (máquina virtual)

##  Procesamiento Batch
Se realiza análisis de datos utilizando Spark sobre un conjunto de datos previamente cargado.

Archivo:
```bash
- batch_analysis.py
```

## Procesamiento en Tiempo Real
Se implementa un sistema de streaming donde:
- Un productor genera datos simulados de sensores
- Kafka transmite los datos
- Spark Streaming procesa la información en tiempo real

Archivos:
```bash
- kafka_producer.py
- spark_streaming_consumer.py
```

## nstrucciones de ejecución

### 1. Iniciar servicios
```bash
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties
```

2. Crear topic
```bash
kafka-topics.sh --create --topic sensor_data --bootstrap-server localhost:9092
```

4. Ejecutar productor
```bash
python3 kafka_producer.py
```

6. Ejecutar consumidor
```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3 spark_streaming_consumer.py
```

Resultados

Se obtienen promedios de temperatura y humedad por sensor en ventanas de tiempo de 1 minuto.

👩‍💻 Autor

Yeli Lizzeth pérez Sepúlveda
