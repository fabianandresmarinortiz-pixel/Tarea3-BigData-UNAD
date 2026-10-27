from pyspark.sql import SparkSession
from pyspark.sql.functions import col, desc

# Iniciar la sesion de Spark
spark = SparkSession.builder \
    .appName("MantenimientoPredictivo_Industrial") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Cargar los datos
print("--- Cargando Dataset de Temperatura de Maquinaria ---")
df = spark.read.csv("machine_temperature_system_failure.csv", header=True, inferSchema=True)
df.printSchema()

# Limpiar y transformar
print("--- Iniciando limpieza de datos ---")
df_transformado = df.withColumnRenamed("value", "temperatura_farenheit")
df_limpio = df_transformado.dropna()

# Analisis exploratorio
print("--- Estadisticas Generales de Operacion ---")
df_limpio.describe(["temperatura_farenheit"]).show()

print("--- Detectando Anomalias (Picos > 90F) ---")
anomalias = df_limpio.filter(col("temperatura_farenheit") > 90.0)
print(f"Total de alertas criticas: {anomalias.count()}")

anomalias.orderBy(desc("temperatura_farenheit")).show(10)

spark.stop()
