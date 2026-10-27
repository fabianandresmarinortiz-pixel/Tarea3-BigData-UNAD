# Análisis en Batch - Mantenimiento Predictivo Industrial con PySpark

Este repositorio contiene el código fuente para el procesamiento en batch de la Tarea 3 del curso de Big Data (UNAD). 

## Descripción del Problema
El script procesa registros históricos de temperatura de sensores en maquinaria industrial para extraer estadísticas de operación y detectar anomalías (temperaturas > 90°F) que indiquen un sobrecalentamiento inminente.

## Conjunto de Datos
Se utiliza el dataset público `machine_temperature_system_failure.csv` perteneciente a datos reales de fallas térmicas.

## Instrucciones de Ejecución
1. Asegúrese de tener Apache Spark instalado y configurado.
2. Descargue el dataset en el mismo directorio del script.
3. Ejecute el análisis en la terminal con el siguiente comando:
   `spark-submit analisis_batch.py`
