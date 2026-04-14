Entorno de trabajo

Todos los comandos y procesos mostrados en este proyecto fueron ejecutados en una máquina virtual previamente configurada con Hadoop y Apache Spark. El acceso a la máquina se realizó mediante conexión SSH utilizando Putty.

Análisis de datos con Spark y Kafka

En este proyecto se realiza el análisis de datos utilizando dos enfoques:

Procesamiento por lotes (batch) con Apache Spark.

Procesamiento en tiempo real (streaming) con Apache Kafka y Spark Streaming.

1. Procesamiento por lotes (Batch)

Se utiliza el archivo batch_analysis.py para agrupar información por sensor y calcular promedios. Ejecútalo con el siguiente comando:

spark-submit batch_analysis.py


Resultado esperado

Se obtienen resultados agregados, tales como:

Promedio de temperatura.

Promedio de humedad.

2. Procesamiento en tiempo real (Streaming)

El flujo de datos funciona así: un Productor genera datos, Kafka los transmite y Spark Streaming los procesa al instante.

Pasos de configuración

A. Instalación de Kafka

Descarga y configura el entorno con estos comandos:

pip install kafka-python
wget [https://downloads.apache.org/kafka/3.8.0/kafka_2.12-3.8.0.tgz](https://downloads.apache.org/kafka/3.8.0/kafka_2.12-3.8.0.tgz)
tar -xzf kafka_2.12-3.8.0.tgz
sudo mv kafka_2.12-3.8.0 /opt/Kafka


B. Iniciar servicios (Usar terminales separadas)

Iniciar ZooKeeper:

sudo /opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties


Iniciar Kafka:

sudo /opt/Kafka/bin/kafka-server-start.sh /opt/Kafka/config/server.properties


C. Crear el Topic

/opt/Kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic sensor_data


3. Ejecución de scripts de Python

Paso 1: Lanzar el Productor de datos

Este archivo (kafka_producer.py) genera datos aleatorios de sensores.

python3 kafka_producer.py


Paso 2: Lanzar el Consumidor (Spark Streaming)

Este archivo (spark_streaming_consumer.py) procesa los datos en tiempo real.

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3 spark_streaming_consumer.py


Resultados obtenidos

Al ejecutar el sistema se pueden observar los promedios de temperatura y humedad organizados en ventanas de tiempo de 1 minuto. Esto demuestra que el sistema está procesando los datos correctamente.
