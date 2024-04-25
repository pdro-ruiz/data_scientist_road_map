# **Funciones en Python**

## **Definición de Funciones**
  - **`def`**
    - Palabra clave utilizada para iniciar la definición de una función.
  - **Nombre de la función**
    - Debe ser descriptivo y adherirse a las convenciones de nombrado de Python (nombres en minúsculas con palabras separadas por guiones bajos para funciones).
  - **Paréntesis**
    - Contienen los argumentos que la función puede aceptar, separados por comas.
  - **Cuerpo de la función**
    - Bloque de código indentado que se ejecuta cuando la función es llamada. Debe mantener una consistencia en la indentación.
  - **Ejemplo**
    - ```python
      def imprime_impares(lista_de_numeros):
          """ Imprime los números impares de una lista dada. """
          for num in lista_de_numeros:
              if num % 2 != 0:
                  print(num)
      ```
      En este ejemplo, `lista_de_numeros` es el parámetro que toma la función, y el cuerpo de la función recorre cada número, imprime los que son impares.

## **Llamada a Funciones**
- Una función se ejecuta utilizando su nombre seguido de paréntesis, que pueden incluir los argumentos necesarios para su operación. Si los argumentos no coinciden con la definición, se generará un error `TypeError` que indica una discrepancia en el número esperado de argumentos.

- **Dinámica de Llamada**
  - **Sin argumentos**: Si no se requieren argumentos, simplemente se utilizan paréntesis vacíos.
  - **Con argumentos**: Los valores pasados deben coincidir en tipo y orden con los que espera la función.

## **Argumentos de Funciones**
- **Tipos de Argumentos**
  - **Posicionales**: Obligatorios y dependen del orden en que se definen.
  - **Con nombre (Keywords)**: Específicos y no dependen del orden.
  - **Predeterminados**: Tienen un valor por defecto que se usa si no se proporciona un argumento.

- **Argumentos Flexibles**
  - **`*args`**: Permite pasar una cantidad variable de argumentos posicionales. Se almacenan como una tupla.
  - **`**kwargs`**: Permite pasar una cantidad variable de argumentos de palabra clave. Se almacenan como un diccionario.
  - **Ejemplo**
    - ```python
        def ejemplo_func(*args, **kwargs):
            print("args:", args)
            print("kwargs:", kwargs)

        ejemplo_func(1, 2, clave1='valor1', clave2='valor2')
        ```

## **Introducción a la Programación Funcional**
- **Conceptos Clave**
  - **Funciones Pura**: En programación funcional, una función pura es aquella que no tiene efectos secundarios (no modifica ningún estado fuera de su alcance local) y devuelve un valor que depende únicamente de sus argumentos.
  - **Inmutabilidad**: Los datos no deben ser modificados una vez creados. En su lugar, cualquier transformación sobre los datos produce nuevos datos.
  - **Funciones de Primera Clase**: Las funciones en Python son tratadas como cualquier otro objeto, lo que significa que pueden ser asignadas a variables, pasadas como argumentos a otras funciones, y retornadas como valores de otras funciones.

  - **Funciones Lambda**
    - Son funciones anónimas, definidas con la palabra clave `lambda`.
    - Son útiles para crear funciones pequeñas y de uso único sin necesidad de la sintaxis formal `def`.
    - **Ejemplo**
      - ```python
          incrementar = lambda x: x + 1
          print(incrementar(3))  # Output: 4
        ```

- **Uso Avanzado de Lambdas**
  - **`map()`**: Transforma cada elemento de una secuencia.
  - **`filter()`**: Filtra elementos de una secuencia.
  - **`reduce()`**: Reduce una secuencia a un único valor.
  - **Ejemplo Práctico con `map` y `filter`**
    - ```python
        numeros = [1, 2, 3, 4, 5]
        cuadrados = list(map(lambda x: x**2, numeros))
        impares = list(filter(lambda x: x % 2 != 0, numeros))

        print("Cuadrados:", cuadrados)  # [1, 4, 9, 16, 25]
        print("Impares:", impares)      # [1, 3, 5]
        ```