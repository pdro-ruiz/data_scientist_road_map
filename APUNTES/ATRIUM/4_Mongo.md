---
title: Mongo
markmap:
  colorFreezeLevel: 3
  maxWidth: 600
---
# MongoDB y Bases de Datos NoSQL

## **Bases de Datos**

### **SQL**
- **Definición y características**
  - SQL (Structured Query Language) es un lenguaje de programación utilizado para gestionar y manipular bases de datos relacionales.
  - **Características principales**:
    - Esquema fijo y estructurado en tablas.
    - Soporte para transacciones ACID (Atomicidad, Consistencia, Aislamiento, Durabilidad).
    - Relaciones entre tablas mediante claves primarias y foráneas.
- **Uso en la industria**
  - Utilizado ampliamente en sistemas financieros, ERP, CRM, y otras aplicaciones empresariales donde la integridad y la consistencia de los datos son críticas.

### **NoSQL**
- **Definición y diferencias con SQL**
  - NoSQL (Not Only SQL) abarca una variedad de tecnologías de bases de datos diseñadas para manejar datos semi-estructurados y no estructurados.
  - **Diferencias con SQL**:
    - No tienen un esquema fijo.
    - Escalan horizontalmente.
    - Se diseñan para manejar grandes volúmenes de datos y alta concurrencia.
- **Casos de uso específicos**
  - Aplicaciones web y móviles que requieren alta escalabilidad y flexibilidad.
  - Big data y análisis en tiempo real.
  - Internet de las cosas (IoT) y datos generados por dispositivos.

## **Tipos de Bases de Datos NoSQL**

### **Columnar**
- **Ejemplos**: Cassandra, BigTable, HBase
- **Características**:
  - Almacenamiento en columnas en lugar de filas.
  - Optimización para consultas de lectura masiva y escritura en grandes volúmenes de datos.
- **Ejemplo de uso**:
  ```sql
  -- Ejemplo de consulta en Apache Cassandra
  SELECT * FROM users WHERE user_id = '1234';
  ```

### **Clave-Valor**
- **Ejemplos**: Redis, Riak KV
- **Características**:
  - Almacenamiento de pares clave-valor.
  - Ideal para datos simples y consultas rápidas.
- **Ejemplo de uso**:
  ```python
  # Ejemplo de uso en Redis
  import redis
  r = redis.Redis(host='localhost', port=6379, db=0)
  r.set('user:1000', 'John Doe')
  print(r.get('user:1000'))
  ```

### **Documental**
- **Ejemplos**: MongoDB, CouchDB
- **Características**:
  - Almacenamiento de datos en formato JSON o BSON.
  - Ideal para datos semi-estructurados y consultas flexibles.
- **Ejemplo de uso**:
  ```python
  # Ejemplo de uso en MongoDB
  from pymongo import MongoClient
  client = MongoClient('localhost', 27017)
  db = client.test_database
  collection = db.test_collection
  document = {"name": "John", "age": 30, "city": "New York"}
  collection.insert_one(document)
  ```

### **Grafos**
- **Ejemplos**: Neo4j, InfiniteGraph
- **Características**:
  - Modelado de datos en nodos y relaciones.
  - Ideal para analizar redes sociales, recomendaciones y otros datos altamente conectados.
- **Ejemplo de uso**:
  ```cypher
  // Ejemplo de consulta en Neo4j
  MATCH (a:Person)-[:FRIEND]->(b:Person)
  WHERE a.name = 'John'
  RETURN b;
  ```

### **Orientado a Objetos**
- **Características**:
  - Almacenamiento de objetos completos como se utilizan en la programación orientada a objetos.
  - Menos común, pero útil para ciertas aplicaciones especializadas.
- **Ejemplo de uso**:
  ```java
  // Ejemplo de uso en una base de datos orientada a objetos
  db.store(new Person("John", "Doe"));
  ```

## **Ventajas de NoSQL**
- **Flexibilidad en el esquema de datos**
  - Permite ajustar el esquema a medida que evolucionan los requisitos de la aplicación.
- **Escalabilidad horizontal**
  - Permite distribuir la carga de trabajo entre múltiples servidores, lo que facilita el manejo de grandes volúmenes de datos.
- **Alta disponibilidad y tolerancia a fallos**
  - Diseñadas para ofrecer alta disponibilidad mediante la replicación y la partición de datos.

## **MongoDB**

### **Definición y características**
- MongoDB es una base de datos NoSQL orientada a documentos que almacena datos en formato BSON (Binary JSON).
- **Características**:
  - Almacenamiento flexible y escalable.
  - Consultas avanzadas y agregaciones.
  - Soporte para replicación y particionamiento de datos.

### **Estructura de datos en MongoDB**
- **Base de datos**: Conjunto de colecciones.
- **Colecciones**: Conjunto de documentos.
- **Documentos**: Estructura JSON o BSON.
- **Campos y tipos de datos soportados**: Strings, números, booleans, arrays, objetos, fechas, binarios, etc.

### **Ventajas y casos de uso**
- Ideal para aplicaciones que requieren alta flexibilidad en el esquema de datos.
- Uso en aplicaciones web, big data, análisis en tiempo real, IoT.

### **Instalación y uso básico**
- **Instalación en Windows y Linux**
  - Descargar desde [MongoDB](https://www.mongodb.com/try/download/community).
  - Seguir las instrucciones del instalador.
- **Uso de MongoDB Compass para administración gráfica**
  - Descargar MongoDB Compass desde el mismo enlace.
  - Conectarse a la instancia de MongoDB y administrar colecciones y documentos gráficamente.
- **Uso de la Shell de MongoDB para comandos**
  - Acceso a la Shell mediante `mongosh` para ejecutar comandos y scripts.
  - **Ejemplo**:
    ```shell
    # Conexión a la shell de MongoDB
    mongosh
    # Crear una base de datos y colección
    use mydatabase
    db.createCollection("mycollection")
    # Insertar un documento
    db.mycollection.insertOne({"name": "John", "age": 30})
    ```

### **Operaciones CRUD en MongoDB**
#### **Crear y Leer**
- **Insertar un documento**:
  ```js
  db.myCollection.insertOne({name: "John", age: 22, location: "Colombo"})
  ```
- **Leer documentos**:
  ```js
  db.myCollection.find()
  ```
- **Filtrar documentos**:
  ```js
  db.myCollection.find({age: {$lt: 25}})
  ```

#### **Actualizar y Eliminar**
- **Actualizar un documento**:
  ```js
  db.myCollection.updateOne({name: "John"}, {$set: {age: 23}})
  ```
- **Eliminar un documento**:
  ```js
  db.myCollection.deleteOne({name: "John"})
  ```

### **Índices en MongoDB**
- **Crear índices para mejorar el rendimiento de las consultas**.
  ```js
  db.myCollection.createIndex({name: 1})
  ```
- **Índice único**:
  ```js
  db.myCollection.createIndex({user_id: 1}, {unique: true})
  ```

### **Consultas avanzadas en MongoDB**
- **Filtrado avanzado**:
  - Operadores de comparación: `$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`
    ```js
    db.myCollection.find({age: {$gte: 21}})
    ```
  - Operadores lógicos: `$and`, `$or`, `$not`, `$nor`
    ```js
    db.myCollection.find({
      $and: [
        {age: {$gte: 21}},
        {location: "Colombo"}
      ]
    })
    ```
  - Operadores de evaluación: `$regex`, `$mod`, `$exists`, `$type`
    ```js
    db.myCollection.find({name: {$regex: "^J"}})
    ```

- **Proyección de campos**:
  - Seleccionar campos específicos en los resultados
    ```js
    db.myCollection.find({}, {name: 1, age: 1, _id: 0})
    ```

- **Consultas de arrays**:
  - Operadores de arrays: `$all`, `$elemMatch`, `$size`
    ```js
    db.myCollection.find({tags: {$all: ["mongodb", "database"]}})
    db.myCollection.find({comments: {$elemMatch: {author: "John", votes: {$gte: 5}}}})
    db.myCollection.find({tags: {$size: 3}})
    ```

- **Consultas de subdocumentos**:
  - Acceso a datos en subdocumentos
    ```js
    db.myCollection.find({"address.city": "New York"})
    ```

- **Consultas de texto**:
  - Búsqueda de texto completo usando índices de texto
    ```js
    db.myCollection.createIndex({content: "text"})
    db.myCollection.find({$text: {$search: "MongoDB"}})
    ```

- **Agregaciones**:
  - Uso del framework de agregación para análisis y transformación de datos
    ```js
    db.sales.aggregate([
      {$match: {status: "A"}},
      {$group: {_id: "$

item", totalSaleAmount: {$sum: "$amount"}}},
      {$sort: {totalSaleAmount: -1}}
    ])
    ```

### **Acceso a MongoDB desde Python usando PyMongo**
#### **Instalación**
- Instalar PyMongo:
  ```bash
  pip install pymongo
  ```

#### **Conexión a MongoDB**
- Crear un cliente de MongoDB y conectarse a una base de datos:
  ```python
  from pymongo import MongoClient
  client = MongoClient('localhost', 27017)
  db = client.prueba
  ```

#### **Operaciones CRUD en PyMongo**
- **Crear documentos**:
  ```python
  post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"], "date": datetime.datetime.utcnow()}
  db.posts.insert_one(post)
  ```

- **Leer documentos**:
  ```python
  for post in db.posts.find():
      print(post)
  ```

- **Actualizar documentos**:
  ```python
  db.posts.update_one({"author": "Mike"}, {"$set": {"text": "My updated blog post!"}})
  ```

- **Eliminar documentos**:
  ```python
  db.posts.delete_one({"author": "Mike"})
  ```

#### **Agregaciones en PyMongo**
- Realizar operaciones de agregación para agrupar y resumir datos.
  ```python
  result = db.posts.aggregate([
      {"$group": {"_id": "$author", "count": {"$sum": 1}}}
  ])
  for doc in result:
      print(doc)
  ```

## **Comparación SQL vs NoSQL**
- **Relacional vs Documental**
  - SQL utiliza un esquema relacional con tablas, mientras que NoSQL (documental) utiliza documentos JSON/BSON.
- **Esquema fijo vs Flexible**
  - SQL requiere un esquema definido, mientras que NoSQL permite esquemas flexibles y dinámicos.
- **Transacciones ACID vs Consistencia eventual**
  - SQL garantiza transacciones ACID, mientras que NoSQL puede ofrecer consistencia eventual para mejorar la escalabilidad.
- **Ejemplos de casos de uso**
  - **SQL**: Aplicaciones financieras, ERP
    - **Ejemplo de consulta SQL**:
      ```sql
      SELECT * FROM transactions WHERE account_id = '1234';
      ```
  - **NoSQL**: Aplicaciones web, big data, IoT
    - **Ejemplo de consulta NoSQL** (MongoDB):
      ```python
      db.transactions.find({"account_id": "1234"})
      ```
