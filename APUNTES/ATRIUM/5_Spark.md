# **Procesamiento Distribuido**

    - **Introducción**
        - **Transición de Bases de Datos a Procesamiento Distribuido**
            - Hemos aprendido sobre bases de datos; ahora es el momento de sumergirnos en el procesamiento distribuido.
            - El procesamiento distribuido es esencial para manejar grandes volúmenes de datos (Big Data) de manera eficiente.
            - Aplicaciones prácticas incluyen análisis en tiempo real, procesamiento de grandes volúmenes de transacciones, y más.
        - **Importancia en Big Data**
            - Big Data requiere métodos de procesamiento eficientes para manejar grandes volúmenes, variedad y velocidad de datos.
            - El procesamiento distribuido permite dividir tareas entre múltiples máquinas, reduciendo el tiempo de procesamiento.
        - **Aplicaciones en el Mundo Real**
            - Ejemplos incluyen el análisis de datos de redes sociales, procesamiento de transacciones financieras, análisis de datos de sensores IoT, etc.

    - **Conceptos**
        - **Escalado y Distribución**
            - **Escalado Horizontal**: Añadir más máquinas para distribuir la carga de trabajo.
            - **Coordinación de Máquinas Pequeñas**: Uso de muchas máquinas pequeñas y económicas, coordinadas entre sí para realizar tareas complejas.
        - **Límites de una Sola Máquina**
            - Limitaciones físicas para escalar una sola máquina.
            - Ejemplo: Las grandes empresas utilizan sistemas distribuidos para manejar grandes volúmenes de datos.

    - **Sistemas y Software**
        - **Apache Hadoop**
            - Importancia histórica y evolución.
            - Componentes: HDFS (Hadoop Distributed File System), YARN (Yet Another Resource Negotiator), MapReduce.
        - **Apache Spark**
            - Alternativa moderna a Hadoop MapReduce.
            - Ventajas: procesamiento más rápido, facilidad de programación.

    - **Consideraciones Prácticas**
        - **Cuándo Usar Procesamiento Distribuido**
            - Adecuado para conjuntos de datos masivos (Big Data).
            - No necesario para conjuntos de datos pequeños.
        - **Ejemplos del Mundo Real**: Bancos procesando transacciones, procesamiento de datos IoT.

    - **Ecosistema de Hadoop**
        - **HDFS (Hadoop Distributed File System)**
            - Almacenamiento de grandes conjuntos de datos.
            - Replicación de datos para tolerancia a fallos.
            - Vista a alto nivel: un solo disco lógico que abarca múltiples máquinas.
        - **MapReduce**
            - Modelo de programación para procesar grandes conjuntos de datos.
            - Pasos: Map, Shuffle, Reduce.
            - Ejemplo: Algoritmo de conteo de palabras.

    - **Apache Spark**
        - **Resumen**
            - Procesamiento en memoria para un cálculo más rápido.
            - Modelo de programación simplificado en comparación con Hadoop MapReduce.
        - **Componentes**
            - Spark Core: funcionalidad básica.
            - Spark SQL: trabajar con datos estructurados.
            - Spark Streaming: procesamiento de datos en tiempo real.
            - MLlib: biblioteca de aprendizaje automático.
            - GraphX: procesamiento de grafos.

    - **Flujo de Trabajo de Procesamiento de Datos**
        - **Ingestión**
            - Herramientas: Apache Kafka, Apache Flume.
            - Ingestión de datos en tiempo real.
        - **Gestión de Recursos**
            - YARN: asignación de recursos en clusters.
            - Mesos: otro gestor de recursos.
        - **Procesamiento y Almacenamiento**
            - Casos de uso para HDFS, S3 y otros sistemas de almacenamiento.
            - Marcos de procesamiento: Spark, MapReduce.

    - **Gestión de Clústeres**
        - **Arquitectura Maestro-Esclavo**
            - Nodo maestro: coordina el clúster.
            - Nodos esclavos: ejecutan tareas.
        - **Tolerancia a Fallos**
            - Estrategias de replicación de datos.
            - Manejo de fallos de nodos.
        - **Localidad de Datos**
            - Importancia de procesar los datos donde están almacenados.
            - Minimizar la comunicación en red para mayor eficiencia.

    - **Programación en MapReduce**
        - **Fase de Map**
            - Aplicar una función a cada elemento de los datos.
        - **Fase de Shuffle**
            - Ordenar y agrupar resultados intermedios.
        - **Fase de Reduce**
            - Agregar resultados para producir la salida final.
        - **Ejemplo de Flujo de Trabajo**
            - Entrada dividida, tareas Map, Shuffle y Sort, tareas Reduce.

    - **Detalles de HDFS**
        - **Almacenamiento en Bloques**
            - Los archivos grandes se dividen en bloques más pequeños.
            - Tamaño de bloque predeterminado: 128MB.
        - **Replicación**
            - Factor de replicación predeterminado: 3.
            - Asegura la disponibilidad de los datos y la tolerancia a fallos.
        - **Operaciones de Archivos**
            - Comandos similares al sistema de archivos Unix (por ejemplo, put, get, rm).

    - **Implementación Práctica**
        - **Configuración de Hadoop y Spark**
            - Pasos de instalación.
            - Consejos de configuración.
        - **Programas de Ejemplo**
            - Conteo de palabras en Hadoop MapReduce.
            - Transformación de datos usando Spark.

    - **Temas Avanzados**
        - **Procesamiento en Tiempo Real con Spark Streaming**
            - Manejo de datos en streaming.
            - Casos de uso: análisis en tiempo real, monitoreo.
        - **Aprendizaje Automático con Spark MLlib**
            - Entrenamiento de modelos en datos distribuidos.
            - Ejemplo: regresión logística, árboles de decisión.
        - **Procesamiento de Grafos con GraphX**
            - Análisis de datos de grafos.
            - Ejemplo: análisis de redes sociales.



```markdown
# Programación con Apache Spark y Python (PySpark)

## Introducción a Apache Spark

- **Apache Spark** es una plataforma de procesamiento distribuido de datos de código abierto.
- Diseñada para ser rápida y general, permite el procesamiento en memoria, lo que acelera las tareas comparado con Hadoop MapReduce.
- Spark soporta diversos lenguajes de programación, incluyendo Java, Scala, Python, y R, siendo Python uno de los más populares debido a su facilidad de uso.

## Configuración de Apache Spark en Google Colab

Para evitar configuraciones complejas en entornos locales, utilizaremos Google Colab con el siguiente código para instalar Spark:
```python
!pip install pyspark
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-2.4.5-bin-hadoop2.7"
!wget -q https://archive.apache.org/dist/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz
!tar xf spark-2.4.5-bin-hadoop2.7.tgz
```
Después de ejecutar este código, Spark estará listo para usarse en Google Colab.

## Creación de DataFrames en Spark

### Desde una lista
```python
from pyspark.sql import SparkSession

# Crear una sesión de Spark
spark = SparkSession.builder.master("local").appName("Ejemplo").getOrCreate()

# Crear DataFrame desde una lista
data = [("Juan", 34), ("Ana", 29), ("Pedro", 45)]
columns = ["Nombre", "Edad"]
df = spark.createDataFrame(data, schema=columns)
df.show()
```

### Desde un CSV
```python
# Leer un archivo CSV
df_csv = spark.read.csv("/ruta/al/archivo.csv", header=True, inferSchema=True)
df_csv.show()
```

## Operaciones Básicas con DataFrames

### Selección y Filtrado
```python
# Seleccionar una columna
df.select("Nombre").show()

# Filtrar datos
df.filter(df["Edad"] > 30).show()
```

### Añadir y Modificar Columnas
```python
from pyspark.sql.functions import col

# Añadir una nueva columna
df = df.withColumn("Edad_Años", col("Edad") + 1)
df.show()

# Renombrar una columna
df = df.withColumnRenamed("Edad", "Edad_Actual")
df.show()
```

### Agregaciones
```python
# Agrupar por una columna y calcular la media
df.groupBy("Edad_Actual").avg("Edad_Años").show()

# Contar valores
df.groupBy("Nombre").count().show()
```

## Uso de Funciones en Spark

### Funciones de SQL
```python
from pyspark.sql.functions import sum, avg, max, min

# Sumar una columna
df.select(sum("Edad_Actual")).show()

# Media de una columna
df.select(avg("Edad_Actual")).show()
```

### Funciones Condicionales
```python
from pyspark.sql.functions import when

# Crear una columna condicional
df = df.withColumn("Categoria", when(df["Edad_Actual"] < 30, "Joven").otherwise("Adulto"))
df.show()
```

## Ejemplo Práctico

Trabajaremos con un dataset de cotización en bolsa de Walmart (`Walmart_Stock.csv`). Realizaremos varias operaciones para practicar lo aprendido:

1. **Cargar el Dataset**
    ```python
    df = spark.read.csv("Walmart_Stock.csv", header=True, inferSchema=True)
    df.show(5)
    ```

2. **Mostrar el Esquema**
    ```python
    df.printSchema()
    ```

3. **Calcular la Media y Desviación Estándar de 'Close'**
    ```python
    from pyspark.sql.functions import stddev
    df.select(avg("Close"), stddev("Close")).show()
    ```

4. **Crear una Nueva Columna 'High/Volume'**
    ```python
    df = df.withColumn("High/Volume", col("High") / col("Volume"))
    df.show(5)
    ```

5. **Filtrar y Mostrar Datos**
    ```python
    df.filter(df["Close"] > 80).show()
    ```

6. **Calcular el Valor Máximo de 'High' por Año**
    ```python
    from pyspark.sql.functions import year

    df.groupBy(year("Date").alias("Year")).max("High").show()
    ```

## Conclusión

Hemos visto cómo configurar y utilizar Spark con Python (PySpark) para realizar operaciones básicas con DataFrames, así como algunas funciones avanzadas para el análisis de datos. Esta guía proporciona una base sólida para comenzar a trabajar con Spark en entornos distribuidos.
```

Para una mayor comprensión de los conceptos y capacidades de PySpark, es útil profundizar en ejemplos adicionales y características más avanzadas de Spark, tales como:

- **Operaciones Avanzadas de DataFrames**
    - **Joins (Uniones)**
        ```python
        # Left Join
        df_left = df1.join(df2, df1["id"] == df2["id"], "left")
        df_left.show()

        # Right Join
        df_right = df1.join(df2, df1["id"] == df2["id"], "right")
        df_right.show()

        # Inner Join
        df_inner = df1.join(df2, df1["id"] == df2["id"], "inner")
        df_inner.show()

        # Full Outer Join
        df_full = df1.join(df2, df1["id"] == df2["id"], "outer")
        df_full.show()
        ```

    - **Transformaciones y Acciones**
        ```python
        # Map Function
        rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
        rdd_map = rdd.map(lambda x: x * 2)
        print(rdd_map.collect())

        # Filter Function
        rdd_filter = rdd.filter(lambda x: x % 2 == 0)
        print(rdd_filter.collect())

        # Reduce Function
        rdd_reduce = rdd.reduce(lambda x, y: x + y)
        print(rdd_reduce)
        ```

    - **Ventanas de Tiempo (Window Functions)**
        ```python
        from pyspark.sql.window import Window
        from pyspark.sql.functions import row_number

        window_spec = Window.partitionBy("column1").orderBy("column2")
        df = df.withColumn("row_number", row_number().over(window_spec))
        df.show()
        ```

    - **Funciones UDF (User Defined Functions)**
        ```python
        from pyspark.sql.functions import udf
        from pyspark.sql.types import IntegerType

        def incrementar(valor):
            return valor + 1

        incrementar_udf = udf(incrementar, IntegerType())
        df = df.withColumn("columna_incrementada", incrementar_udf(df["columna"]))
        df.show()
        ```

- **Spark SQL**
    - Ejecución de consultas SQL directamente en DataFrames.
        ```python
        df.createOrReplaceTempView("tabla")
        spark.sql("SELECT * FROM tabla WHERE columna > 50").show()
        ```

- **Machine Learning con Spark MLlib**
    - Introducción a la creación y entrenamiento de modelos de Machine Learning con Spark MLlib.

        ```python
        from pyspark.ml.classification import LogisticRegression

        # Cargar datos y dividir en conjunto de entrenamiento y prueba
        data = spark.read.format("libsvm").load("/ruta/a/datos.libsvm")
        train, test = data.randomSplit([0.8, 0.2], seed=1234)

        # Crear y entrenar el modelo
        lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)
        lr_model = lr.fit(train)

        # Realizar predicciones
        predictions = lr_model.transform(test)
        predictions.show()
        ```

Para profundizar más, es recomendable consultar la [documentación oficial de PySpark](https://spark.apache.org/docs/latest/api/python/index.html) y seguir tutoriales adicionales específicos para las tareas y datos que se trabajarán en proyectos futuros.
```