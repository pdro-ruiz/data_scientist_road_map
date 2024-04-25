# Presentacion

## 1. Introducción al Big Data

### Los datos como activo

#### Análisis Descriptivo
- **Objetivo**: Resumir grandes cantidades de datos para facilitar la comprensión y la toma de decisiones.
- **Teoría**: Utiliza métodos estadísticos para describir y sintetizar datos sin establecer relaciones de causa-efecto.
- **Aplicación práctica**: Utilizado en reportes de ventas o rendimiento de marketing para identificar tendencias o patrones.

#### Análisis Predictivo
- **Objetivo**: Pronosticar eventos futuros basándose en datos históricos mediante técnicas estadísticas y de modelado.
- **Teoría**: Incluye modelos estadísticos y de aprendizaje automático que aprenden de datos pasados para predecir resultados futuros.
- **Aplicación práctica**: Predicción de demanda de productos, identificación de riesgos crediticios en bancos, o anticipación de fallos en mantenimiento de equipos.

#### Análisis Prescriptivo
- **Objetivo**: Sugerir decisiones y mostrar las consecuencias de cada decisión.
- **Teoría**: Combina técnicas de optimización y simulación con análisis predictivo para encontrar soluciones óptimas.
- **Aplicación práctica**: Optimización de rutas logísticas, gestión avanzada de inventarios, y configuración de precios dinámicos.

### Herramientas para Análisis Descriptivo

#### Científicos de Datos
- **Herramientas**: Lenguajes como Python, R, y MATLAB.
- **Uso**: Manipulación de datos, realización de cálculos estadísticos complejos, y desarrollo de modelos predictivos.

#### Analistas de Negocio
- **Herramientas de BI**: Power BI, Qlik Sense, Tableau.
- **Uso**: Creación de dashboards interactivos y visualizaciones para análisis no técnico.

#### Ventajas del Análisis Descriptivo
- Neutralidad en el manejo de datos, amplio alcance de exploración de eventos, y precisión en la recolección y descripción de relaciones entre datos.

#### Inconvenientes del Análisis Descriptivo
- Riesgo de sesgos en la investigación, dificultades para incorporar datos no esperados, y el peligro de generalizaciones apresuradas.

### Enlaces a Recursos Académicos y Estudios de Caso
- [Análisis predictivo en el sector financiero](https://ejemplo-link-finanzas.com)
- [Uso de BI en marketing](https://ejemplo-link-marketing.com)
- [Evolución histórica del análisis de datos](https://ejemplo-link-historia.com)

### Conceptos Matemáticos Aplicados en Análisis Descriptivo
- **Estadística Descriptiva**: Incluye medidas de tendencia central como la media, mediana, y modo; medidas de dispersión como la varianza y desviación estándar.
- **Ejemplo Práctico**: Análisis de las ventas mensuales de una empresa para determinar el rendimiento estándar y detectar anomalías o picos en las ventas.





## 2. Introducción a las Bases de Datos Big Data

### Creación de Tecnología e Infraestructura para el Big Data

#### Fundamentos de Infraestructura para Big Data
- **Objetivo**: Establecer sistemas que permitan almacenar, consultar y analizar grandes volúmenes de datos.
- **Componentes Clave**:
  - **Almacenamiento**: Uso de diversas bases de datos según el tipo de datos.
  - **Procesamiento**: Infraestructura tecnológica como servidores y clústeres.

#### Tipos de Información en Big Data
- **Datos Estructurados**: Información en formatos tradicionales como bases de datos SQL, fáciles de organizar y analizar.
- **Datos No Estructurados**: Información en formatos no convencionales como videos, imágenes y textos, que requieren herramientas especializadas para su análisis.
- **Datos Semiestructurados**: Combinación de estructurados y no estructurados, como JSON o XML.

### Almacenamiento y Consulta de Datos

#### Datos Estructurados
- **Almacenamiento en RDBMS (Relational Database Management System)**:
  - **Modelo Relacional**: Organización de datos en tablas que se relacionan entre sí.
  - **Operaciones CRUD (Crear, Leer, Actualizar, Borrar)**:
    - **Insert**: Añadir nuevos registros.
    - **Select**: Consultar registros existentes.
    - **Update**: Actualizar datos.
    - **Delete**: Eliminar datos.
  - **Propiedades ACID**:
    - **Atomicidad**: Las transacciones son completas o no ocurren.
    - **Consistencia**: Solo se permiten transacciones que llevan la base de datos de un estado válido a otro.
    - **Aislamiento**: Transacciones ejecutadas concurrentemente resultan en un sistema en estado estable.
    - **Durabilidad**: Una vez que una transacción se ha completado, los cambios son permanentes.

#### Datos No Estructurados
- **Herramientas y Técnicas**:
  - Uso de sistemas como Hadoop y bases de datos NoSQL para manejar la variedad y volumen.

### Herramientas NoSQL
- **Tipos de Bases de Datos NoSQL**:
  - **Documentales**: Almacenan datos en documentos similares a JSON (MongoDB, CouchDB).
  - **Clave-Valor**: Almacenan datos en un esquema de clave-valor (Redis, DynamoDB).
  - **Columnares**: Optimizadas para leer y escribir datos en columnas en lugar de filas (Cassandra).
  - **De Grafos**: Utilizan estructuras de grafos para representar y almacenar datos (Neo4j).
- **Ventajas de NoSQL**:
  - Escalabilidad horizontal, flexibilidad en los tipos de datos, y menor latencia en las respuestas.

### Enlaces a Literatura Académica y Estudios de Caso
- [Explorando las Bases de Datos NoSQL para Big Data](https://academic-link-noSQL.com)
- [Uso de MongoDB en Aplicaciones de Big Data](https://case-study-mongoDB.com)

### Representaciones Matemáticas y Lógicas
- **Modelado de Datos NoSQL**:
  - **Teorema CAP**: Explicación sobre Consistencia, Disponibilidad y Tolerancia a Particiones.
  - **Ejemplos**: Modelado de cómo se aplican estas propiedades en escenarios de bases de datos distribuidas.

### Resumen y Conclusión
- **Relevancia de Bases de Datos en Big Data**: Discusión sobre cómo las bases de datos estructuradas y NoSQL facilitan la manipulación de datos a gran escala.
- **Desafíos Futuros**: Identificación de áreas emergentes en la gestión de datos grandes como la seguridad, la integración de IA y las mejoras en la eficiencia del procesamiento.




## 3. Introducción al procesamiento distribuido y la Cloud

### Tecnologías Big Data - Ingesta de Datos
#### Conceptos Clave
- **Ingesta de Datos**: Proceso de obtener e importar datos para análisis inmediato o almacenamiento.
- **Métodos**: Datos pueden ser ingeridos en tiempo real o en lotes.
- **Procesos de Ingesta**:
  1. **Extracción**: Recolectar datos desde la fuente.
  2. **Transformación**: Validar, limpiar y normalizar datos para asegurar precisión y confiabilidad.
  3. **Carga**: Almacenar datos en el destino adecuado para su análisis futuro.

#### Ejemplo de Aplicación Práctica
- Monitoreo de datos de salud en tiempo real donde la latencia baja es crucial para decisiones rápidas y efectivas.

#### Enlaces Relevantes
- [Estudio de caso sobre la ingestión de datos en tiempo real en la atención médica](https://healthcare-data-ingestion.com)

### Tecnologías Big Data - Procesamiento Distribuido de Datos
#### Fundamentos Teóricos
- **Procesamiento Distribuido**: División de datos en múltiples nodos para procesamiento en paralelo, mejorando la eficiencia y velocidad.
- **Modelos Clave**: MapReduce, utilizado para distribuir tareas a múltiples máquinas y gestionar la comunicación y transferencia de datos.

#### Ejemplo de Código
```python
def map_function(data):
    # Procesa y organiza los datos en función de un parámetro
    return processed_data

def reduce_function(data):
    # Resumen y combinación de los datos procesados
    return summarized_data
```
- **Análisis**: La función `map` procesa datos individualmente mientras que `reduce` los combina para formar un resultado global.

#### Enlaces a Recursos Académicos
- [Deep Dive into MapReduce](https://mapreduce-example.com)

### Tecnologías Big Data - Cloud Computing
#### Aspectos Teóricos
- **Cloud Computing**: Provisión de recursos informáticos a través de internet, permitiendo escalabilidad y flexibilidad.
- **Modelos de Servicio**:
  1. **IaaS**: Infraestructura como servicio.
  2. **PaaS**: Plataforma como servicio.
  3. **SaaS**: Software como servicio.

#### Representación Matemática y Lógica
- **Elasticidad en la nube**: Matemáticamente, puede modelarse como \( C(n) = a \times n \) donde \( n \) es el número de unidades de recurso y \( a \) es un factor de escala.

#### Enlaces de Estudio Profundo
- [Optimización de recursos en la nube](https://cloud-resource-optimization.com)

### Conclusión
- **Integración y Futuro**: La interrelación entre Big Data, procesamiento distribuido y computación en la nube forma el futuro de la tecnología, permitiendo a las empresas no solo almacenar y analizar grandes volúmenes de datos, sino también hacerlo de manera eficiente y rentable.

#### Enlaces para Exploración Adicional
- [Tecnologías emergentes en Big Data y Cloud](https://future-tech.com)
