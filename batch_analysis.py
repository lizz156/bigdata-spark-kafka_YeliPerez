from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("BatchAnalysis") \
    .getOrCreate()

# Simulación de datos
data = [
    (1, 25.5, 40),
    (2, 26.0, 50),
    (1, 24.8, 45),
    (2, 27.1, 55)
]

columns = ["sensor_id", "temperature", "humidity"]

df = spark.createDataFrame(data, columns)

# Promedios por sensor
result = df.groupBy("sensor_id").avg()

result.show()