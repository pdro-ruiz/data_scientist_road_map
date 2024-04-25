# Excepciones en Python

## Definición y Tipos de Errores

- En Python, las excepciones son errores detectados durante la ejecución del programa, a diferencia de los errores sintácticos que se detectan en el tiempo de compilación. Hay dos tipos principales de errores:

- **Errores Sintácticos:** Estos ocurren cuando el código no sigue la sintaxis correcta de Python.
- **Excepciones:** Estos son errores detectados durante la ejecución que interrumpen el flujo normal del programa.

## Ejemplos de Excepciones Comunes

- **ZeroDivisionError:** Ocurre al intentar dividir cualquier número por cero.
- **NameError:** Se produce cuando una variable no está definida.
- **TypeError:** Resulta de una operación o función aplicada a un objeto de tipo inapropiado.

## Manejo de Excepciones
- El manejo de excepciones en Python se realiza a través de los bloques `try` y `except`. Esto permite que el programa continúe incluso después de que ocurra un error.

    - ```python
        try:
            # Código que puede lanzar una excepción
            x = 1 / 0
        except ZeroDivisionError:
            # Código que se ejecuta si hay una excepción
            print("No se puede dividir por cero.")
        ```

## Especificando Excepciones
- Python permite especificar múltiples tipos de excepciones en el bloque `except` para manejar diferentes errores de manera diferente.

   -  ```python
        try:
            x = int(input("Introduce un número entero: "))
        except ValueError:
            print("Eso no es un entero.")
        except (TypeError, NameError):
            print("Error de tipo o NameError detectado.")
        ```

## Cláusulas `else` y `finally`

- **Else:** Se ejecuta si el bloque `try` no lanza una excepción.
- **Finally:** Se ejecuta después de los bloques `try` y `except`, independientemente de si se lanzó una excepción o no.

    - ```python
        try:
            print("Intentamos ejecutar el bloque try:")
            x = 1 / 1
        except:
            print("Algo salió mal...")
        else:
            print("¡Todo bien!")
        finally:
            print("El bloque 'finally' siempre se ejecuta.")
        ```

## Lanzamiento de Excepciones

- Se pueden lanzar excepciones intencionadamente usando la palabra clave `raise`. Esto es útil para crear verificaciones y hacer que el programa falle deliberadamente bajo condiciones específicas.

   - ```python
        x = 10
        if x > 5:
            raise Exception("x no debe exceder de 5. El valor de x fue: {}".format(x))
        ```

## Definición de Excepciones Personalizadas
- Se pueden crear excepciones personalizadas mediante la definición de clases que se derivan de la clase Exception. Esto permite crear excepciones que son específicas para las necesidades del programa.

    - ```python
        class MiError(Exception):
            def __init__(self, valor):
                self.valor = valor
            def __str__(self):
                return repr(self.valor)

        try:
            raise MiError(2*2)
        except MiError as e:
            print('Mi excepción ocurrió, valor:', e.valor)
        ```