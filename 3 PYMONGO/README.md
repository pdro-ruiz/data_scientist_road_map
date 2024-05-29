# Objetivo de la Práctica 

En esta práctica utilizaremos la misma colección que hemos utilizado en los ejercicios resueltos:

## Documento de muestra de la colección 'restaurants':

```json
{
  "address": {
     "building": "1007",
     "coord": [ -73.856077, 40.848447 ],
     "street": "Morris Park Ave",
     "zipcode": "10462"
  },
  "borough": "Bronx",
  "cuisine": "Bakery",
  "grades": [
     { "date": { "$date": 1393804800000 }, "grade": "A", "score": 2 },
     { "date": { "$date": 1378857600000 }, "grade": "A", "score": 6 },
     { "date": { "$date": 1358985600000 }, "grade": "A", "score": 10 },
     { "date": { "$date": 1322006400000 }, "grade": "A", "score": 9 },
     { "date": { "$date": 1299715200000 }, "grade": "B", "score": 14 }
  ],
  "name": "Morris Park Bake Shop",
  "restaurant_id": "30075445"
}
```

## Tareas a Realizar

El estudiante debe crear un notebook de Jupyter que haga lo siguiente:

### 1. Conexión a la Base de Datos
Nos conectamos, mediante `pymongo`, a la base de datos y a la colección que creamos para los ejercicios resueltos.

### 2. Consultas
Realizamos las mismas consultas que ya hicimos en los ejercicios de MongoDB.

### 3. Visualización Sencilla de los Datos
Generamos gráficos con `matplotlib` que muestren la distribución de valores de `borough` y `cuisine`. Los posibles valores de cada variable y su número de registros asociados deben generarse mediante una consulta en `pymongo`.

### 4. Inserción de Datos
Insertamos todos los nuevos restaurantes almacenados en `new_restaurants.json`.

### 5. Añadir Nuevos Campos a los Documentos
Creamos un valor raíz en cada documento con el nombre `avg_score`, que contiene el valor medio de `puntuación` de ese restaurante. Si no se han encontrado valores para realizar este cálculo, ponemos en su lugar un valor Nulo. Se puede hacer de dos maneras el cálculo, o bien con una query de Mongo o bien haciendo cada cálculo con Python y insertando los resultados.

### (Extra y Opcional) Visualización de Datos Geográficos
Generamos un archivo png de un mapa que muestra puntos coloreados con las coordenadas de cada restaurante. Debe utilizar un color diferente por tipo de `cocina`. Puede utilizar algo como esto para crear el mapa.