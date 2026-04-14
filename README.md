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

Procesamiento en Tiempo Real (Kafka + Spark Streaming)
1. Instalación de Kafka

```bash
pip install kafka-python
wget https://downloads.apache.org/kafka/3.8.0/kafka_2.12-3.8.0.tgz
tar -xzf kafka_2.12-3.8.0.tgz
sudo mv kafka_2.12-3.8.0 /opt/Kafka
```

2. Iniciar servicios

Iniciar ZooKeeper
```bash
sudo /opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties
```

Iniciar Kafka
```bash
sudo /opt/Kafka/bin/kafka-server-start.sh /opt/Kafka/config/server.properties
```

3. Crear Topic en Kafka
```bash
/opt/Kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic sensor_data
```

4. Productor de datos (Kafka)

Archivo:

kafka_producer.py

Este script genera datos simulados de sensores (temperatura y humedad) y los envía a Kafka.

```bash
python3 kafka_producer.py
```

5. Consumidor con Spark Streaming

Archivo:

spark_streaming_consumer.py

Este script consume los datos desde Kafka y realiza procesamiento en tiempo real.

```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3 spark_streaming_consumer.py
```

Resultados

Durante la ejecución se observan resultados como:

Promedio de temperatura por sensor
Promedio de humedad por sensor
Procesamiento en ventanas de 1 minuto

Ejemplo:

Sensor 5 → temperatura promedio ≈ 25°C
Humedad promedio ≈ 49%

Esto demuestra el análisis en tiempo real de los datos.

👩‍💻 Autor

Yeli Lizzeth pérez Sepúlveda
