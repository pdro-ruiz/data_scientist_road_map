
# Sentencias básicas de Python

## Expresiones, sentencias y variables

- **Expresiones y sentencias**: Diferenciación y ejemplos.
- **Variables**:
  - Declaración y asignación.
  - Tipos de datos no necesitan ser especificados explícitamente.
  - Ejemplos de declaración y reasignación.

**Ejemplos prácticos**:

- `print("Hola Mundo")`: Uso de print para mostrar mensajes.
- `a = 10`: Asignación de un valor a una variable.
- `type(a)`: Verificación del tipo de una variable.

**Notas de aplicación**:

- Importancia de la indentación en Python.
- Python es un lenguaje no tipado dinámicamente.

## Trabajando con números

- **Tipos numéricos**: integer, float, complex.
- **Operaciones aritméticas**: Suma, resta, multiplicación, división, etc.

**Ejemplos prácticos**:

- `1 + 1`: Suma de enteros.
- `10 / 2`: División que resulta en un float.
- `2 ** 10`: Potenciación.

**Notas de aplicación**:

- Python realiza conversiones automáticas entre tipos numéricos en operaciones aritméticas.
- Uso de `type()` para verificar el tipo de los datos.

## Trabajando con Strings

- **Creación de strings**: Uso de comillas simples o dobles.
- **Concatenación y manipulación de strings**.

**Ejemplos prácticos**:

- `"Hola" + " Mundo"`: Concatenación de strings.
- `cadena[1:5]`: Acceso a subcadenas.

**Notas de aplicación**:

- Los strings en Python son inmutables.
- Métodos comunes para la manipulación de strings: `upper()`, `lower()`, `strip()`, `split()`, etc.


## Trabajando con booleanos

- **Definición**: El tipo booleano en Python define los valores `True` y `False`.
- **Operadores admitidos**:
  - **OR**: `True or False` → `True`
  - **AND**: `True and False` → `False`
  - **NOT**: `not False` → `True`
- **Operaciones lógicas**:
  - Comparaciones como `<`, `>`, `==`, `!=`, `>=`, `<=`.
  - `1 < 1` → `False`
  - `1 == 1` → `True`
- **Operadores de identidad**:
  - **is**: `1 is 1` → `True`
  - **is not**: `1 is not 1.0` → `True`

### Ejemplos prácticos y notas de aplicación

- La diferencia entre `==` y `is`: `==` compara valores mientras `is` compara si dos variables apuntan al mismo objeto o valor.
- Uso de `is not` para la comparación de identidad negada.

## Trabajando con listas

- **Definición**: Colecciones ordenadas de elementos que pueden ser de distintos tipos.
- **Características**:
  - Mutables.
  - Accesibles por índice.
  - Se pueden concatenar y repetir usando `+` y `*`.

### Ejemplos prácticos

- Creación de listas: `list_1 = ["a", "b", "c"]`.
- Acceso por índice: `list_1[0]` → `"a"`.
- Concatenación: `list_1 + [1, 2, 3]` → `['a', 'b', 'c', 1, 2, 3]`.
- Repetición: `list_1 * 2` → `['a', 'b', 'c', 'a', 'b', 'c']`.

### Notas de aplicación y métodos comunes

- `list.append(x)`: Agrega un elemento al final.
- `list.extend(iterable)`: Extiende la lista agregando todos los elementos del iterable al final.
- `list.insert(i, x)`: Inserta un elemento en la posición `i`.
- `list.remove(x)`: Elimina el primer elemento cuyo valor sea `x`.
- `list.pop([i])`: Elimina el elemento en la posición `i` y lo devuelve.
- `list.clear()`: Elimina todos los elementos de la lista.
- `list.sort()`, `list.reverse()`: Ordena o invierte los elementos de la lista en su lugar.

## Trabajando con tuplas

- **Definición**: Colecciones inmutables de elementos de cualquier tipo.
- **Características**:
  - Ordenadas.
  - Acceso por índice.
  - Inmutables.

### Ejemplos prácticos

- Creación de tuplas: `t_1 = ("a", "b", "c")`.
- Acceso por índice: `t_1[0]` → `"a"`.
- Concatenación: `t_1 + (1, 2, 3, 4)` → `('a', 'b', 'c', 1, 2, 3, 4)`.
- Repetición: `t_1 * 2` → `('a', 'b', 'c', 'a', 'b', 'c')`.

## Trabajando con diccionarios

- **Definición**: Estructuras de datos que mapean claves únicas a valores.
- **Características**:
  - Las claves son únicas e inmutables.
  - Los valores pueden ser de cualquier tipo.
  - Orden de inserción mantenido en Python 3.7+.

### Ejemplos prácticos y notas de aplicación

- Creación: `dict_1 = {"clave_1": "valor_1", "clave_2": "valor_2"}`.
- Acceso: `dict_1["clave_1"]` → `"valor_1"`.
- Añadir o actualizar: `dict_1["clave_3"] = "valor_3"`.
- Eliminar: `del dict_1["clave_3"]`.

## Trabajando con conjuntos (set)

- **Definición**: Colecciones desordenadas de elementos únicos.
- **Características**:
  - Cada elemento es único.
  - Los elementos deben ser inmutables.
  - No garantizan un orden.

### Operaciones básicas de conjuntos

- Unión: `set_1 | set_2`.
- Intersección: `set_1 & set_2`.
- Diferencia: `set_1 - set_2`.
- Diferencia simétrica: `set_1 ^ set_2`.

### Ejemplos prácticos y notas de aplicación

- Creación: `set_1 = {1, 2, 3}`.
- Añadir elementos: `set_1.add(4)`.
- Eliminar elementos: `set_1.remove(4)` o `set_1.discard(4)`.
