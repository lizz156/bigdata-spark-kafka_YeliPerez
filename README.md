## Entorno de trabajo

Todos los comandos y procesos mostrados en este proyecto fueron ejecutados en una máquina virtual previamente configurada con Hadoop y Apache Spark, proporcionada en las actividades anteriores del curso.
El acceso a la máquina se realizó mediante conexión SSH utilizando Putty.

---

# Análisis de datos con Spark y Kafka

En este proyecto se realiza el análisis de datos utilizando dos enfoques:

- Procesamiento por lotes (batch) con Apache Spark
- Procesamiento en tiempo real (streaming) con Apache Kafka y Spark Streaming

El objetivo es entender cómo se pueden procesar datos históricos y también datos en tiempo real simulando información de sensores.

---

## Procesamiento por lotes (Batch)

Para esta parte se utilizó Spark con el fin de analizar datos y obtener resultados agregados.

Archivo utilizado:
- batch_analysis.py

Este script permite agrupar la información por sensor y calcular valores como el promedio.

### Ejecución

```bash
spark-submit batch_analysis.py

---
### Resultado esperado

Se obtienen resultados agrupados por sensor, por ejemplo:

Promedio de temperatura
Promedio de humedad

---
### Procesamiento en tiempo real (Streaming)

En esta parte se implementa un flujo de datos en tiempo real utilizando Kafka y Spark Streaming.

El proceso funciona de la siguiente manera:

Un productor genera datos simulados
Kafka recibe y transmite los datos
Spark Streaming procesa la información en tiempo real


---
Pasos realizados
1. Instalación de Kafka
Se descarga y configura Kafka en la máquina virtual:

pip install kafka-python
wget https://downloads.apache.org/kafka/3.8.0/kafka_2.12-3.8.0.tgz
tar -xzf kafka_2.12-3.8.0.tgz
sudo mv kafka_2.12-3.8.0 /opt/Kafka

---
pip install kafka-python
wget https://downloads.apache.org/kafka/3.8.0/kafka_2.12-3.8.0.tgz
tar -xzf kafka_2.12-3.8.0.tgz
sudo mv kafka_2.12-3.8.0 /opt/Kafka

---
2. Iniciar servicios

Primero se inicia ZooKeeper:

sudo /opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties

---
Luego se inicia Kafka:

sudo /opt/Kafka/bin/kafka-server-start.sh /opt/Kafka/config/server.properties

---
3. Crear el topic

Se crea el canal donde se enviarán los datos:

/opt/Kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic sensor_data

---
4. Productor de datos

Archivo:

kafka_producer.py

Este programa genera datos aleatorios de sensores (temperatura y humedad) y los envía a Kafka constantemente.

python3 kafka_producer.py

---

5. Consumidor con Spark Streaming

Archivo:

spark_streaming_consumer.py

Este programa lee los datos desde Kafka y los procesa en tiempo real agrupándolos por ventanas de tiempo.

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3 spark_streaming_consumer.py

----
Resultados obtenidos

Al ejecutar el sistema se pueden observar resultados en la consola donde se muestran:

Promedios de temperatura por sensor
Promedios de humedad por sensor
Datos organizados en ventanas de tiempo de 1 minuto

Por ejemplo:

Sensor 5 → temperatura promedio cercana a 25°C
Humedad promedio cercana al 49%

Esto demuestra que el sistema está procesando los datos en tiempo real correctamente.


