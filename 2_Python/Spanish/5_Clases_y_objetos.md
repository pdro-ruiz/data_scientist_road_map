# 5. Clases y Objetos

## Introducción
- **Relevancia**: Facilita la organización del código y la reutilización de software.

## Conceptos Fundamentales
### Clases y Objetos
- **Clase**: Plantilla para crear objetos que define un conjunto de atributos y métodos relacionados.
  ```python
  class Punto:
      def __init__(self, x, y):
          self.x = x
          self.y = y
      def __str__(self):
          return f"({self.x}, {self.y})"
  ```
  - *Comentario*: `__init__` es el constructor que inicializa los atributos del objeto.

### Métodos Especiales
- **Sobrecarga de Operadores**:
  - **Suma** (`__add__`):
    ```python
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)
    ```
  - **Resta** (`__sub__`):
    ```python
    def __sub__(self, otro):
        return Punto(self.x - otro.x, self.y - otro.y)
    ```
  - *Comentario*: Estos métodos permiten que los objetos de clase `Punto` interactúen con operadores `+` y `-`.

### Trabajo con Iteradores
- **Generadores**:
  - **Uso de `yield`**:
    ```python
    class MultiplesGenerator:
        def __init__(self, base, limit):
            self.base = base
            self.limit = limit
        def __iter__(self):
            num = 0
            while self.base * num < self.limit:
                yield self.base * num
                num += 1
    ```
  - *Comentario*: `yield` permite generar valores uno a uno, útil para secuencias grandes sin ocupar mucha memoria.

## Recursos Adicionales
- [Tutorial de Python sobre Clases y Objetos](https://docs.python.org/3/tutorial/classes.html)
- [Explicación sobre Métodos Mágicos en Python](https://www.python-course.eu/python3_magic_methods.php)

## Visualizaciones y Ejemplos Matemáticos
- **Diagrama de Clase `Punto`**:
  | Método       | Descripción                             |
  |--------------|-----------------------------------------|
  | `__init__`   | Constructor, inicializa x e y.          |
  | `__add__`    | Permite sumar dos puntos.               |
  | `__sub__`    | Permite restar dos puntos.              |
  | `__str__`    | Método para representar el punto como cadena. |




  