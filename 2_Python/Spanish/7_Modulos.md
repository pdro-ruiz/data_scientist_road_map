# Módulos

## Definicion
- Los módulos en Python son fundamentales para estructurar programas de manera más legible y mantenible.
  
## Importación de Módulos

- **Uso Básico**:  
  `import time`  
  Accedes a funciones con `time.función()`.
  
- **Importación Específica**:  
  `from sys import copyright`  
  Permite usar `copyright` directamente.
  
- **Alias en Importaciones**:  
  `from sys import copyright as c`  
  Ahora `c` representa `copyright`.

- **Importar Todo con Comodín**:  
  `from sys import *`  
  Importa todo de `sys`, aunque no es recomendado por razones de claridad y posibles conflictos de nombres.

## Creación de Módulos

- **Crear un Módulo Propio**:  
  Simplemente crea un archivo `.py` (ej. `fibo.py`) que contenga funciones y variables.

- **Uso del Módulo Creado**:  
  `import fibo`  
  Utiliza funciones con `fibo.nombre_función()`.

- **Funciones de Ayuda**:  
  `help(fibo.fib_print)`  
  Muestra la documentación y detalles del módulo `fibo`.

- **Importar Funciones Específicas**:  
  `from fibo import fib, fib_print`  
  Permite usar `fib()` y `fib_print()` directamente sin prefijo.

### Cómo Distinguir entre Módulos y el Programa Principal

- **Uso de `__name__`**:  
  Si `__name__ == "__main__"`:  
  Este bloque se ejecuta solo si el archivo es el programa principal.

### Paquetes de Módulos

- **Estructura de Directorios**:  
  Organiza los módulos en paquetes con estructuras de directorio que reflejen su uso y relaciones.

- **Ejemplo de Estructura**:  
  ```
  sound/
  ├── __init__.py
  ├── formats/
  │   ├── __init__.py
  │   ├── wavread.py
  │   ├── wavwrite.py
  ├── effects/
  │   ├── __init__.py
  │   ├── echo.py
  ├── filters/
  │   ├── __init__.py
  │   ├── equalizer.py
  ```

- **Importar de Paquetes**:  
  `from sound.effects import echo`

### Añadiendo nuevos paquetes y módulos

- **Añadir al PYTHONPATH**:  
  Configura `PYTHONPATH` para incluir directorios donde están tus módulos o paquetes para que Python los reconozca.


