# Objetivo de la Práctica 

Dado el siguiente dataset:

[Dataset de Seguro Médico](https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv)

Cuyas variables representan:

- **age**: edad del beneficiario principal
- **sex**: género del contratante del seguro, femenino, masculino
- **bmi**: índice de masa corporal, que proporciona una comprensión del cuerpo, de los pesos que son relativamente altos o bajos en relación con la altura, índice objetivo de peso corporal (kg / m²) utilizando la relación entre la altura y el peso, idealmente entre 18,5 y 24,9.
- **children**: número de hijos cubiertos por el seguro de salud / número de dependientes
- **smoker**: si fuma o no
- **region**: área de residencia del beneficiario en EE. UU., noreste, sureste, suroeste, noroeste.
- **charges**: costos médicos individuales facturados por el seguro de salud.

## 1. Primera Parte (6 puntos)

Utilizando la API de pandas de PySpark:

```python
import pyspark.pandas as ps
```

Realiza un EDA (Análisis Exploratorio de Datos) del dataset anterior.

## 2. Segunda Parte (4 puntos)

Luego conviértelos a un DataFrame de Spark normal, realiza las conversiones necesarias para poder hacer machine learning (`StringIndexer`, `StandardScaler`, `VectorAssembler`...) y aplica un modelo de regresión lineal usando `pyspark.ml`.

La variable objetivo a predecir sería `charges`.

**NOTA**: En el caso de que hayáis sido incapaces de instalar adecuadamente Spark, podéis usar Spark en Google Colab poniendo lo siguiente en la primera celda:

```bash
!pip install pyspark
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
```

```python
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
```
