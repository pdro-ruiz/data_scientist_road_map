# Bloques Lógicos en Python

## Condiciones: `if`, `if-else`, `if-elif`

### Funcionamiento Detallado:
- **`if` Statement**: Es la estructura de control básica que permite ejecutar un bloque de código sólo si una condición dada es verdadera. Python evalúa la condición y, si el resultado es `True`, ejecuta el bloque de código indentado bajo el `if`.
- **`elif` (else if)**: Proporciona condiciones adicionales que se evalúan si las anteriores son falsas. Si la condición en el `elif` es verdadera, se ejecutará el bloque de código correspondiente.
- **`else`**: Captura cualquier caso que no cumpla las condiciones anteriores. No lleva condición y su bloque se ejecuta si todos los `if` y `elif` anteriores evaluaron a `False`.

### Ejemplo en Profundidad:
Supongamos que queremos evaluar el rendimiento de un estudiante:

```python
puntuacion = 82

if puntuacion >= 90:
    print("Excelente")
elif puntuacion >= 75:
    print("Bueno")  # Este bloque se ejecutará
elif puntuacion >= 50:
    print("Aceptable")
else:
    print("Mejor esfuérzate más")
```

## Bucles

### `for` - Iteraciones sobre secuencias
  - **Propósito**: 
    - Iterar sobre una secuencia (como una lista, tupla, cadena o rango) y ejecutar un bloque de código para cada elemento.
  - **Aplicaciones**:
    - Iterar sobre rangos de números.
    - Leer elementos de una lista o tupla.
    - Extraer claves o valores de un diccionario.
    
  -  **Ejemplo**:
      ```python
      for numero in range(1, 6):
          print(numero)
      ```

### List Comprehension
  - **Propósito**:
    - Proporcionar una manera concisa de crear listas.
  - **Ventajas**:
    - Menos líneas de código.
    - Menor propensión a errores.
    - Mejorada legibilidad (para expresiones simples).

  -  Ejemplo:
       - Supongamos que queremos crear una lista de los cuadrados de números pares del 1 al 10:

         ```python
         cuadrados_pares = [x**2 for x in range(1, 11) if x % 2 == 0]
         print(cuadrados_pares)  # [4, 16, 36, 64, 100]
         ```

### Iteradores
  - **Concepto**: 
    - Un objeto que sigue el protocolo del iterador, que incluye métodos `__iter__()` y `__next__()`.
  - **`__iter__()`**: 
    - Devuelve el objeto iterador.
  - **`__next__()`**: 
    - Devuelve el siguiente elemento de la colección. Cuando se alcanza el final de la colección, este método debe lanzar una excepción `StopIteration`.
  - Ejemplo:
      - ```python
        class Contador:
            def __init__(self, bajo, alto):
                self.actual = bajo
                self.alto = alto

            def __iter__(self):
                return self

            def __next__(self):
                if self.actual < self.alto:
                    num = self.actual
                    self.actual += 1
                    return num
                raise StopIteration

        contador = Contador(3, 8)
        for num in contador:
            print(num)  # Imprime números de 3 a 7
        ```

### Generadores

#### Concepto:
- Un generador es una herramienta que permite a Python generar datos de manera perezosa (lazy), es decir, uno a la vez y solo a demanda. Esto es especialmente útil en situaciones donde:
  - No es posible o práctico tener todos los datos en la memoria.
  - Se requiere un proceso iterativo donde el conjunto de datos es grande o potencialmente infinito.

#### Creación de Generadores:
- Los generadores se pueden crear de dos maneras principales en Python:
1. **Expresiones de generador**, que son sintácticamente similares a las comprensiones de listas pero con paréntesis en lugar de corchetes.
2. **Funciones generadoras**, que utilizan la palabra clave `yield` para devolver valores uno a la vez.

#### Expresiones de Generador:
- Las expresiones de generador son una forma simple de crear generadores sin la necesidad de una función. Se utilizan para operaciones sencillas sobre secuencias.

- **Ejemplo de Expresión de Generador:**
  - ```python
    # Generador para obtener números impares hasta 20
    odds = (x for x in range(1, 20) if x % 2 != 0)
    print(next(odds))  # 1
    print(next(odds))  # 3
    ```
    En este ejemplo, `odds` es un generador. Utilizando `next()`, podemos obtener el siguiente valor impar de la secuencia sin necesidad de generar todos los impares a la vez.

#### Funciones Generadoras:
- Una función generadora es similar a una función regular, pero utiliza `yield` para devolver datos. Este enfoque es útil cuando el proceso de generación es complejo o involucra estados.

- Ejemplo de Función Generadora:
    - ```python
      def generar_impares(hasta):
          num = 1
          while num < hasta:
              if num % 2 != 0:
                  yield num
              num += 1

      impares = generar_impares(20)
      print(next(impares))  # 1
      print(next(impares))  # 3
      ```

#### Ventajas de los Generadores:
- **Eficiencia de memoria**: Los generadores no cargan toda la secuencia en memoria, sino que generan los elementos bajo demanda.
- **Eficiencia computacional**: Reducen el tiempo de espera antes de comenzar a procesar, especialmente útil en flujos de datos o archivos muy grandes.

### Bucle `while`

#### Descripción:
- El bucle `while` en Python repite un bloque de código mientras una condición sea verdadera. Es adecuado para ciclos donde el número de iteraciones no es conocido antes de que comience el bucle.

- **Ejemplo**
  - ```python
    contador = 0
    while contador < 5:
        print(contador)
        contador += 1
    ```

### Break y Continue
- **`break`**: Termina el bucle y transfiere la ejecución al siguiente bloque de código.
- **`continue`**: Omite el resto del código dentro del bucle para la iteración actual y vuelve al inicio del bucle.

- **Ejemplo de `break` y `continue`:**
  - ```python
    n = 0
    while True:
        if n == 3:
            break
        n += 1
        if n == 2:
            continue
        print(n)  # Imprime 1 y 3
    ```

### Pass
- La instrucción `pass` es una operación nula; nada sucede cuando se ejecuta. Es útil en lugares donde la sintaxis requiere una declaración pero la lógica no requiere ninguna acción.

- **Ejemplo**
  - ```python
    for num in range(20):
        if num % 2 == 0:
            pass  # No hacer nada
        else:
            print(num)  # Imprime números impares
    ```