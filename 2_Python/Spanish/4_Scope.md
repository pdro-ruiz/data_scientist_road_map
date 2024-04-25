# **Scope (Ámbito de Variables) y Namespaces en Python**

## **Concepto**
- **Definición**
  - Un namespace es un mapeo donde los nombres se vinculan a objetos, tales como variables, funciones y clases. 
- **Tipos de Namespace**:
  - **Built-in**: Incluye funciones incorporadas (`abs()`, `sum()`) y excepciones (`NameError`).
  - **Global**: Variables y funciones definidas a nivel de módulo.
  - **Local**: Variables dentro de la definición de una función.
  
## **Jerarquía de Namespaces**
- **Built-in Namespace**: El nivel más alto que contiene funciones y excepciones incorporadas.
- **Global Namespace**: Definido a nivel del módulo y accesible desde cualquier lugar dentro del módulo.
- **Local Namespace**: Específico de una función o método y es temporal, existe durante la ejecución de esa función.

## **Ejemplos de Namespaces**
1. **Built-in Namespace**: Acceso directo a funciones como `abs()`.
    - ```python
        print(abs(-1))  # Salida: 1
        ```
2. **Global Namespace**: Variables definidas en el módulo.
    - ```python
        A = 1
        print(A)  # Salida: 1
        ```
3. **Local Namespace**: Variables dentro de una función.
   - ```python
      B = 4
      def mi_fun():
          B = 1
          print(B)  # Salida: 1 (Accede a la versión local de B)
      mi_fun()
      ```

## **Independencia de Namespaces**
- Los nombres en diferentes namespaces pueden ser iguales sin conflicto.
- Para acceder a nombres desde módulos específicos se debe calificar el acceso con el nombre del módulo, especialmente relevante cuando se trabaja con múltiples módulos que pueden tener nombres en conflicto.

## **Acceso y Duración de los Namespaces**
- **Namespace Global**
  - Se crea cuando se lee un módulo y permanece hasta que el intérprete termina.
- **Namespace Local**
  - Se crea al invocar una función y se elimina al finalizar la ejecución de la función, ya sea normalmente o por una excepción.

## **Scope (Ámbito)**
- **Definición**: El scope es una región del código donde un namespace es accesible directamente sin prefijos.
- **Regla LEGB para la Resolución de Nombres**:
  - **Local (L)**
    - Nombres asignados dentro de una función (no declarados global ni nonlocal).
  - **Enclosed (E)**
    - Nombres en el scope de cualquier función envolvente (`def` o `lambda`), de adentro hacia afuera.
  - **Global (G)**
    - Nombres asignados en el nivel superior del módulo o declarados global en una def dentro del módulo.
  - **Built-in (B)**
    - Nombres preasignados en el módulo built-ins de Python.
  -  **Ejemplo de LEGB**
    - ```python
        variable = 100  # Global

        def funcion():
            variable = 10  # Enclosed

            def funcion_interna():
                variable = 1  # Local
                print("Variable más interna:\t\t", variable)
            
            funcion_interna()
            print("Variable nivel intermedio:\t", variable)

        funcion()
        print("Variable externa:\t\t", variable)
        ```
        Salidas:
        ```
        Variable más interna: 1
        Variable nivel intermedio: 10
        Variable externa: 100
        ```

## **Limitaciones y Comportamiento en Bucles**
- A diferencia de otros lenguajes, los bucles `for` en Python no crean un nuevo scope local. Las variables creadas o modificadas dentro de un bucle son accesibles fuera del mismo.
- **Ejemplo de Scope en Bucles**
  - ```python
    lista = ["a", "b", "c"]
    for elemento in lista:
        elem = elemento
    print(elem)  # Salida: c
    print(elemento)  # Salida: c
    ```