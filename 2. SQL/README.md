# Objetivo de la Práctica 

Crea un notebook de Jupyter y con la librería de SQLite realiza las siguientes consultas a la base de datos "Chinook_Sqlite" (archivo proporcionado junto con los apuntes de SQL).

## Actividad 2-1 (Atención al cliente)

Trabaja con la tabla `Customer`.

1. Muestra la columna `Email`.
2. Muestra la columna `FirstName`.
3. Muestra las columnas `FirstName` y `LastName`.
4. Muestra las columnas `Address`, `Phone` y `Fax`.
5. Muestra todas las columnas.

## Actividad 3-1 (Ordenando a mi manera)

1. Ordena la tabla de géneros (`Genre`) por orden alfabético.
2. Corta los resultados para que solo se muestren los 6 primeros.
3. Subir Nota:
    - Muestra las últimas 2 filas de la tabla.

## Actividad 3-2 (En busca del peor cliente)

Volvemos a usar la tabla `Customer`.

1. Muestra los usuarios que han reportado más de 3 incidencias (columna donde se cuentan es `SupportRepId`).
2. Filtra los resultados anteriores por los que viven en Brasil.
3. Muestra a los usuarios que tengan un código postal empezado en 7.
4. Muestra a los usuarios que tengan un email de hotmail.
5. Muestra los usuarios nacidos en Estados Unidos (USA) o Canadá (Canada).
6. De los resultados anteriores, muestra los que tengan un email de gmail.
7. Muestra al usuario que trabaja en Apple (columna `Company`). Te aviso que no sabes el formato de la compañía, podría ser: Apple SL, Company Apple, APPLE…
8. Muestra los usuarios que han reportado entre 3 y 4 incidencias.

## Actividad 3-3 (Limpieza de personal)

Usaremos la tabla `Employee` (empleados).

1. Cuenta la cantidad de empleados que hay por ciudad.
2. Cuenta la cantidad de empleados que hay por departamento.
3. Subir Nota:
    - Muestra la edad de cada empleado.
    - Calcula la media de edad por departamento (`Title`).
    - Cuenta los empleados que fueron contratados, de media, por año.

## Actividad 4-1 (Experto en canciones)

Volvemos a usar la tabla `Track` (canción).

1. Muestra todas las canciones con el `MediaType` Protected AAC audio file.
2. Muestra todas las canciones que contengan algún `MediaType` con AAC.
3. Muestra todas las canciones que duren más de 2 minutos.
4. Muestra todas las canciones de Jazz.
5. Averigua cuál es la canción más pesada.
6. Subir Nota:
    - ¿Cuántos discos tiene Led Zeppelin?
    - De entre sus discos, ¿cuánto cuesta el disco Houses Of The Holy?

## Actividad 5-1 (Solo compañías)

De la tabla `Customer` crea una vista llamada `Customer_with_companies`, donde estarán incluidos todos los resultados salvo cuando `Company` sea NULL. A partir de la vista realiza las siguientes acciones.

1. Ordena los resultados por orden alfabético de `Company`.
2. Muestra qué compañías son de Brazil.

## Actividad 6-1 (Dame la factura)

De la tabla `Track`, consigue la siguiente información.

1. ¿Cuál es el título de la canción que menos pesa (Bytes)?
2. ¿Cuál es el título de la canción que más dura (Miliseconds)?
3. ¿Cuántas canciones cuestan 1$ o más?
4. ¿Cuántas canciones hay de Queen?
5. ¿Cuál es la media de duración entre todas las canciones?
6. ¿Cuál es la media de peso entre todas las canciones de U2?
7. ¿Cuántas canciones tiene Bill Berry como compositor (`Composer`)?
8. Un Mb son: Bytes / 1024 / 1024. Muestra todos los `Tracks` calculando, y renombrando, la columna `Bytes` en Mb.

## Actividad 7-1 (Buscando facturas)

De la tabla `Invoice`, consigue la siguiente información.

1. Muestra: `InvoiceId`, nombre del cliente y `BillingCountry`.
2. Ordena de mayor a menor por `Total`.
3. ¿Cuál es el país que más ha facturado?

## Actividad 8-1 (Alimentando la productora)

1. Añade 5 artistas que te gusten en la tabla `Artist`.
2. Introduce el `MediaType` Wav.
3. Crea 2 discos que estén relacionados con los artistas que has creado.

## Actividad 9-1 (Artistas desaparecidos)

Volvemos a usar la tabla `Artist`. (usa `PRAGMA foreign_keys = OFF` para desactivar la comprobación)

1. Borra a U2.
2. Borra los artistas que tengan en su nombre el símbolo `&`.
3. Borra los artistas con una `Id` entre 201 y 230.
4. Borra toda la tabla de `Track`.

## Actividad 10-1 (Se acabaron las rebajas)

Volvemos a usar la tabla `Track`.

1. Sube el precio de todas las canciones de 0.99 a 2.99.
2. Sube el precio de todas las canciones de 1.99 a 4.99.
3. Cambia el compositor (`Composer`) por Sara del `TrackId` número 2000.
4. Cambia el compositor (`Composer`) por clásico de todas las canciones que empiecen con el nombre Concerto.
