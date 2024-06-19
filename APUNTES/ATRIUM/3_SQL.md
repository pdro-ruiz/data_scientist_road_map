---
title: SQL
markmap:
  colorFreezeLevel: 3
  maxWidth: 600
---

# SQL

## Introducción 
- SQL (Structured Query Language) es un lenguaje de programación diseñado para gestionar y manipular bases de datos relacionales.
- Es un estándar internacional que permite realizar operaciones como consultas, actualizaciones, eliminaciones e inserciones de datos en una base de datos.
- SQL se utiliza ampliamente en aplicaciones empresariales, sistemas de gestión de bases de datos y análisis de datos.

### Historia
- Desarrollado en los años 70 por IBM en el laboratorio de investigación de San José, California.
- Basado en el modelo relacional propuesto por Edgar F. Codd.
- Primer producto comercial que utilizó SQL: Oracle en 1979.
- Adoptado por DBMS como MySQL, PostgreSQL, SQL Server.

### Fundamentos de las Bases de Datos Relacionales
#### Modelos Relacionales
- Los datos se organizan en tablas que se componen de filas y columnas.
- Cada fila representa un registro único y cada columna representa un campo.
- Las tablas pueden relacionarse entre sí mediante claves primarias y claves foráneas.

#### Tablas
- Una tabla es una colección de datos organizados en un formato de filas y columnas.
- ```sql
  CREATE TABLE clientes (
      cliente_id INT PRIMARY KEY,
      nombre VARCHAR(100),
      correo VARCHAR(100),
      fecha_registro DATE
  );
  ```

#### Filas y Columnas
- Las filas representan instancias únicas de datos dentro de una tabla.
- Las columnas representan atributos de los datos que se almacenan en las filas.
- ```sql
  INSERT INTO clientes (cliente_id, nombre, correo, fecha_registro)
  VALUES (1, 'Juan Pérez', 'juan.perez@example.com', '2024-01-15');
  ```

#### Relaciones entre Tablas
- Se establecen utilizando claves primarias y claves foráneas.
- Clave primaria: campo que identifica de manera única cada fila en una tabla.
- Clave foránea: campo en una tabla que se refiere a la clave primaria en otra tabla.
- ```sql
  CREATE TABLE pedidos (
      pedido_id INT PRIMARY KEY,
      cliente_id INT,
      fecha_pedido DATE,
      FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
  );
  ```

## Comandos Básicos

### SELECT
- Se utiliza para consultar y recuperar datos de una tabla.
- ```sql
  SELECT nombre, correo FROM clientes WHERE fecha_registro > '2023-01-01';
  ```

### INSERT
- Se utiliza para agregar nuevos registros a una tabla.
- ```sql
  INSERT INTO clientes (cliente_id, nombre, correo, fecha_registro)
  VALUES (2, 'Ana Gómez', 'ana.gomez@example.com', '2024-06-18');
  ```

### UPDATE
- Se utiliza para modificar datos existentes en una tabla.
- ```sql
  UPDATE clientes
  SET correo = 'ana.gomez@newdomain.com'
  WHERE cliente_id = 2;
  ```

### DELETE
- Se utiliza para eliminar registros de una tabla.
- ```sql
  DELETE FROM clientes WHERE cliente_id = 2;
  ```

## Consultas Avanzadas

### Funciones de Agregado
- SQL proporciona funciones de agregado para realizar cálculos sobre un conjunto de valores.
- ```sql
  SELECT COUNT(*) FROM clientes; -- Contar el número de registros
  SELECT AVG(total) FROM pedidos; -- Calcular el promedio
  SELECT SUM(total) FROM pedidos; -- Calcular la suma
  SELECT MAX(total) FROM pedidos; -- Encontrar el valor máximo
  SELECT MIN(total) FROM pedidos; -- Encontrar el valor mínimo
  ```

### Cláusulas JOIN
- Se utilizan para combinar filas de dos o más tablas basadas en una condición relacionada.

#### Tipos de JOIN en SQL
- **INNER JOIN**: Devuelve filas cuando hay coincidencias en ambas tablas.
  - ```sql
    SELECT clientes.nombre, pedidos.pedido_id
    FROM clientes
    INNER JOIN pedidos ON clientes.cliente_id = pedidos.cliente_id;
    ```

- **LEFT JOIN**: Devuelve todas las filas de la tabla izquierda y las coincidencias de la tabla derecha. Si no hay coincidencia, devuelve NULL.
  - ```sql
    SELECT clientes.nombre, pedidos.pedido_id
    FROM clientes
    LEFT JOIN pedidos ON clientes.cliente_id = pedidos.cliente_id;
    ```

- **RIGHT JOIN**: Devuelve todas las filas de la tabla derecha y las coincidencias de la tabla izquierda. Si no hay coincidencia, devuelve NULL.
  - ```sql
    SELECT clientes.nombre, pedidos.pedido_id
    FROM clientes
    RIGHT JOIN pedidos ON clientes.cliente_id = pedidos.cliente_id;
    ```

- **FULL JOIN**: Devuelve filas cuando hay coincidencias en una de las tablas. Si no hay coincidencia, devuelve NULL.
  - ```sql
    SELECT clientes.nombre, pedidos.pedido_id
    FROM clientes
    FULL OUTER JOIN pedidos ON clientes.cliente_id = pedidos.cliente_id;
    ```

### Subconsultas
- Las subconsultas son consultas anidadas dentro de otra consulta.
- ```sql
  SELECT nombre
  FROM clientes
  WHERE cliente_id = (
      SELECT cliente_id
      FROM pedidos
      WHERE pedido_id = 1
  );
  ```

### Vistas
- Las vistas son consultas almacenadas que pueden tratarse como tablas virtuales.
- ```sql
  CREATE VIEW clientes_activos AS
  SELECT nombre, correo
  FROM clientes
  WHERE activo = 1;
  ```

### Funciones de Usuario
- SQL permite crear funciones definidas por el usuario para encapsular lógica de consulta compleja.
- ```sql
  CREATE FUNCTION calcular_descuento(precio DECIMAL, descuento DECIMAL)
  RETURNS DECIMAL
  BEGIN
      RETURN precio - (precio * descuento / 100);
  END;
  ```

## Consultas Complejas

### Cláusula WHERE
- Se utiliza para filtrar registros que cumplen una condición específica.
- ```sql
  SELECT nombre, correo
  FROM clientes
  WHERE fecha_registro > '2023-01-01' AND activo = 1;
  ```

### Cláusula GROUP BY
- Se utiliza para agrupar filas que tienen valores iguales en columnas especificadas y permite aplicar funciones de agregado a cada grupo.
- ```sql
  SELECT cliente_id, COUNT(*)
  FROM pedidos
  GROUP BY cliente_id;
  ```

### Cláusula HAVING
- Similar a WHERE, pero se utiliza para filtrar grupos de registros después de aplicar la cláusula GROUP BY.
- ```sql
  SELECT cliente_id, COUNT(*)
  FROM pedidos
  GROUP BY cliente_id
  HAVING COUNT(*) > 5;
  ```

### Cláusula ORDER BY
- Se utiliza para ordenar los resultados de una consulta en orden ascendente o descendente.
- ```sql
  SELECT nombre, fecha_registro
  FROM clientes
  ORDER BY fecha_registro DESC;
  ```

### Cláusula LIMIT
- Se utiliza para limitar el número de filas devueltas por una consulta.
- ```sql
  SELECT nombre, correo
  FROM clientes
  ORDER BY fecha_registro DESC
  LIMIT 10;
  ```

## Integración con Python

### Librerías Populares
- Existen varias librerías en Python que permiten interactuar con bases de datos SQL.
- Librerías populares incluyen `sqlite3`, `SQLAlchemy` y `PyMySQL`.

#### Ejemplo de uso de `sqlite3`
```python
import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('ejemplo.db')
cursor = conn.cursor()

# Crear una tabla
cursor.execute('''
    CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        edad INTEGER
    )
''')

# Insertar datos
cursor.execute('''
    INSERT INTO usuarios (nombre, edad)
    VALUES ('Carlos', 30)
''')

# Consultar datos
cursor.execute('SELECT * FROM usuarios')
for row in cursor.fetchall():
    print(row)

# Cerrar la conexión
conn.close()
```

#### Conexión a Bases de Datos y Ejecución de Consultas
- Ejemplo de conexión a una base de datos MySQL usando `PyMySQL`:
  ```python
  import pymysql

  # Conectar a la base de datos
  conn = pymysql.connect(
      host='localhost',
      user='usuario',
      password='contraseña',
      db='basededatos'
  )
  cursor = conn.cursor()

  # Ejecutar una consulta
  cursor.execute('SELECT * FROM clientes')
  for row in cursor.fetchall():
      print(row)

  # Cerrar la conexión
  conn.close()
  ```

#### Uso de Pandas para Analizar Datos Extraídos de SQL
- Pandas es una biblioteca de Python que proporciona herramientas para la manipulación y el análisis de datos.
- Se integra fácilmente con SQL para realizar consultas y procesar los resultados.
- Ejemplo con SQLite:
  ```python
  import pandas as pd
  import sqlite3

  # Conectar a la base de datos
  conn = sqlite3.connect('ejemplo.db')

  # Leer datos en un DataFrame
  df = pd.read_sql_query("SELECT * FROM usuarios", conn)
  print(df)

  # Cerrar la conexión
  conn.close()
  ```

#### Análisis y Visualización de Datos
- SQL facilita la realización de análisis de datos mediante consultas complejas, agregaciones y filtrado de

 datos.
- Los resultados de las consultas SQL pueden integrarse con herramientas de visualización de datos como matplotlib en Python.
- Ejemplo de SQL con matplotlib:
  ```python
  import sqlite3
  import matplotlib.pyplot as plt

  # Conectar a la base de datos
  conn = sqlite3.connect('ejemplo.db')
  cursor = conn.cursor()

  # Realizar una consulta
  cursor.execute('SELECT nombre, edad FROM usuarios')
  datos = cursor.fetchall()

  # Preparar datos para la visualización
  nombres = [row[0] for row in datos]
  edades = [row[1] for row in datos]

  # Crear una gráfica de barras
  plt.bar(nombres, edades)
  plt.xlabel('Nombre')
  plt.ylabel('Edad')
  plt.title('Edad de los usuarios')
  plt.show()

  # Cerrar la conexión
  conn.close()
  ```

### Comando INSERT INTO
- Se utiliza para agregar nuevos registros a una tabla en una base de datos.
- ```sql
  INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...)
  ```
- ```sql
  INSERT INTO géneros VALUES (NULL, 'Flamenco')
  ```

### Comando DELETE
- Se utiliza para eliminar registros de una tabla en una base de datos.
- ```sql
  DELETE FROM table_name WHERE condition
  ```
- ```sql
  DELETE FROM playlist WHERE Name = 'Audiobooks'
  ```

### Comando UPDATE
- Se utiliza para modificar datos existentes en una tabla.
- ```sql
  UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition
  ```
- ```sql
  UPDATE customers SET Company = 'Facebook' WHERE CustomerID = 10
  ```

## Uso de SQLite con Python

### Configuración Inicial
- Crear una base de datos y abrir una conexión.
- Uso de cursores para ejecutar queries.
- ```python
  import sqlite3
  conn = sqlite3.connect('tutorial.db')
  cursor = conn.cursor()
  ```

### Ejemplos de uso
- Crear una tabla:
  ```sql
  CREATE TABLE movie (title TEXT, year INTEGER, score REAL);
  ```

- Insertar datos:
  ```sql
  INSERT INTO movie VALUES ('Monty Python and the Holy Grail', 1975, 8.2);
  ```

- Ejecutar un commit:
  ```python
  conn.commit()
  ```

- Consultar datos:
  ```sql
  SELECT score FROM movie;
  ```

### Consulta de Datos y Manipulación Avanzada
#### Inserción Masiva
- Uso de `executemany` para insertar múltiples registros.
- ```python
  data = [('Movie1', 1999, 7.8), ('Movie2', 2002, 8.1)]
  cursor.executemany('INSERT INTO movie VALUES (?, ?, ?)', data)
  ```

#### Extracción y Visualización de Datos
- Uso de `fetchall` y `fetchone` para recuperar datos.
- ```python
  cursor.execute('SELECT * FROM movie')
  print(cursor.fetchall())
  ```

## Comandos CREATE TABLE y ALTER TABLE
### Definición
- Crear tabla con restricciones:
  ```sql
  CREATE TABLE album (
      AlbumId INTEGER NOT NULL, 
      Title TEXT NOT NULL, 
      PRIMARY KEY (AlbumId)
  );
  ```

### Modificación de Tablas
- ALTER TABLE:
  ```sql
  ALTER TABLE table_name ADD column_name datatype;
  ```

## Importancia en el Mundo Empresarial

### Gestión Eficiente y Estructurada de Datos
- SQL permite organizar, almacenar y recuperar datos de manera eficiente y estructurada.
- Las empresas utilizan SQL para gestionar grandes volúmenes de datos y realizar análisis complejos.
- Ejemplos de aplicaciones empresariales incluyen sistemas de gestión de clientes (CRM), sistemas de planificación de recursos empresariales (ERP) y sistemas de gestión de inventarios.

### Uso Extendido en Diversas Aplicaciones Empresariales
- SQL es utilizado en diversas industrias, incluyendo finanzas, salud, educación, retail, y tecnología.
- Las habilidades en SQL son altamente demandadas en el mercado laboral, ya que la capacidad de trabajar con bases de datos es esencial para muchas posiciones técnicas y analíticas.
- SQL se integra fácilmente con otros lenguajes de programación y herramientas de análisis de datos, lo que permite a las empresas aprovechar al máximo sus datos.

### Análisis y Visualización de Datos
- SQL facilita la realización de análisis de datos mediante consultas complejas, agregaciones y filtrado de datos.
- Los resultados de las consultas SQL pueden integrarse con herramientas de visualización de datos como Tableau, Power BI y matplotlib en Python.
