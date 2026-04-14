## Entorno de trabajo

Todos los comandos y procesos mostrados en este proyecto fueron ejecutados en una máquina virtual previamente configurada con **Hadoop** y **Apache Spark**. El acceso se realizó mediante conexión **SSH** utilizando Putty.

---

# Análisis de datos con Spark y Kafka

En este proyecto se realiza el análisis de datos utilizando dos enfoques:
* **Batch:** Procesamiento por lotes con Apache Spark.
* **Streaming:** Procesamiento en tiempo real con Apache Kafka y Spark Streaming.

---

## 1. Procesamiento por lotes (Batch)

Se utilizó el archivo `batch_analysis.py` para agrupar información por sensor y calcular promedios. Ejecútalo con:

```bash
spark-submit batch_analysis.py

Resultado esperado
Se obtienen resultados agregados, tales como:

Promedio de temperatura.
Promedio de humedad.

2. Procesamiento en tiempo real (Streaming)
El flujo de datos funciona así: un Productor genera datos, Kafka los transmite y Spark Streaming los procesa al instante.

Pasos de configuración
A. Instalación de Kafka
Ejecuta los siguientes comandos para descargar y configurar el entorno:

pip install kafka-python
wget https://downloads.apache.org/kafka/3.8.0/kafka_2.12-3.8.0.tgz
tar -xzf kafka_2.12-3.8.0.tgz
sudo mv kafka_2.12-3.8.0 /opt/Kafka

B. Iniciar servicios
Es necesario abrir terminales separadas para cada servicio.

Iniciar ZooKeeper:
sudo /opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties
