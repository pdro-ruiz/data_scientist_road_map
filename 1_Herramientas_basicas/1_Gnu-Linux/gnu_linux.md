# **Linux Shell Essentials**

## Introducción

1. **¿Qué es GNU/Linux?**
   - Sistema operativo tipo Unix, multiplataforma, multiusuario y multitarea.
   - Combina proyectos como GNU de la Free Software Foundation y el kernel Linux de Linus Torvalds.
   - Representa un prominente ejemplo de software libre: código abierto modificable y redistribuible.

2. **Origen de GNU/Linux**
   - **Proyecto GNU (1983)**
     - Iniciado por Richard Stallman para crear un sistema operativo compuesto enteramente de software libre, como alternativa libre a Unix.
   - **Kernel Linux (1991)**
     - Desarrollado por Linus Torvalds, integrado con herramientas GNU para formar el sistema operativo GNU/Linux.
   - Comúnmente conocido como "Linux".

3. **¿Qué es UNIX?**
   - Sistema operativo portable, multitarea y multiusuario desarrollado en 1969 por AT&T Bell Labs.
   - Filosofía UNIX: Crear programas especializados que intervengan mínimamente con el usuario, adecuados para ambientes científicos.

4. **¿Qué es una Distribución GNU/Linux?**
   - Compendios que incluyen el sistema operativo junto con una selección de aplicaciones, conocidos como distribuciones o "distros".

5. **Entornos Gráficos de Escritorio**
   - GNU/Linux permite usar múltiples entornos gráficos, siendo los más populares **GNOME** y **KDE**.

6. **¿Qué es una Shell?**
   - Interfaz de usuario para acceder a los servicios del sistema operativo, generalmente se refiere a intérpretes de línea de comandos.

7. **Bash (Bourne-again shell)**
   - Lenguaje de comandos y shell de Unix desarrollado para el Proyecto GNU como reemplazo del shell Bourne.
   - Bash es el intérprete de comandos más usado en Linux y será el enfoque principal de aprendizaje en este curso.

## Comandos Básicos en Bash

1. **Navegación**
   - `cd`, `ls`, `pwd`: Comandos para cambiar directorios, listar contenidos y mostrar el directorio actual.

2. **Gestión de Archivos**
   - `touch`, `mkdir`, `rm`, `cp`, `mv`: Comandos para crear, eliminar, copiar y mover archivos y directorios.

3. **Permisos y Propiedades**
   - `chmod`, `chown`: Comandos para cambiar los permisos y el propietario de archivos y directorios.

4. **Redirección y Piping**
   - `>`, `>>`, `|` para redirigir salidas de comandos a archivos o como entrada a otros comandos.

5. **Scripts de Bash**
   - Creación y ejecución de scripts simples para automatizar tareas.

## Herramientas y Recursos Adicionales

1. **Editores de Texto**
   - `nano`, `vim` para editar scripts y archivos de configuración.

2. **Gestión de Paquetes**
   - `apt` para instalar, actualizar y remover software.

3. **Búsqueda y Ayuda**
   - `man`, `info`, `whatis` para obtener ayuda y documentación sobre comandos y configuraciones.


## Conceptos Básicos

### 1. Repositorios de Software
- **Función**: 
  - Servidores que alojan aplicaciones y actualizaciones necesarias para el sistema.
- **Ventajas**:
  - Mantenimiento de software actualizado y compatible.
  - Reducción de redundancias y optimización de recursos.
  - Mayor seguridad al evitar software obsoleto.
- **Dependencias**
  - Los paquetes de software pueden requerir otros paquetes para funcionar correctamente.
- **Tipos de Repositorios**
  - Oficiales
  - no-oficiales.

### 2. Gestores de Paquetes
- **Función**
  - Facilitan la instalación, actualización y desinstalación de software desde los repositorios.
- **Ejemplo en Ubuntu**:
  - `apt` (Advanced Packaging Tool).
  - Interfaz de línea de comandos y GUI (Ubuntu Software).
- **Comandos Básicos de `apt`**:
  - `sudo apt-get update`: Actualiza la lista de paquetes.
  - `sudo apt-get upgrade`: Instala actualizaciones disponibles.
  - `sudo apt-get install [paquete]`: Instala un paquete.
  - `sudo apt-get remove [paquete]`: Desinstala un paquete.

### 3. La Jerarquía del Sistema de Archivos de Linux
- **Root (`/`)**: Punto de partida del sistema de archivos, similar a `C:\` en Windows pero sin letras de unidad.
- **Directorios Importantes**:
  - `/bin`: Binarios esenciales del usuario.
  - `/sbin`: Binarios esenciales de administración del sistema.
  - `/lib`: Librerías necesarias para los binarios en `/bin` y `/sbin`.
  - `/boot`: Contiene archivos necesarios para el arranque del sistema.
  - `/dev`: Representa dispositivos como archivos, incluye pseudodispositivos como `/dev/null`.
  - `/home`: Directorios personales de los usuarios.
  - `/media`: Punto de montaje para medios extraíbles.
  - `/proc`: Información del sistema y procesos en forma de archivos.
  - `/root`: Directorio del usuario root.
  - `/tmp`: Almacena archivos temporales.
  - `/usr`: Aplicaciones y datos no esenciales para el arranque del sistema.
  - `/var`: Datos variables y archivos de log.

### 4. Sistemas de Archivos
- **Formatos Comunes en Linux**:
  - `ext4`: Sistema de archivos extendido versión 4, común en Linux.
  - `XFS`: Sistema de archivos con escalabilidad y rendimiento.

### 5. Sistema de Permisos
- **Propietarios**:
  - `User`: El creador del archivo, que tiene control total sobre él.
  - `Group`: Grupo de usuarios que comparten permisos.
  - `Other`: Todos los demás usuarios del sistema.
- **Tipos de Permisos**:
  - `Read`: Permite leer el archivo o listar el contenido de un directorio.
  - `Write`: Permite modificar el archivo o alterar el contenido de un directorio.
  - `Execute`: Permite ejecutar un archivo como programa.


## La Shell de Linux

### Conceptos Clave de Bash y Shell
- **Bash (Bourne-Again SHell)**: Es un intérprete de comandos para varios sistemas operativos, siendo el predeterminado en la mayoría de los sistemas GNU/Linux.
- **Shell**: Procesador de comandos que facilita la ejecución de instrucciones en el sistema operativo.
- **Scripting**: Creación de archivos ejecutables (.sh) que permiten la ejecución automática de comandos.

### Uso de Comandos en Bash
- **Directo en terminal**: Ejecutar comandos individualmente.
- **Scripts**: Secuencias de comandos guardadas en un archivo para ejecución automática.
- **Opciones y Argumentos**:
  - Opciones (`-`): Modifican el comportamiento de los comandos.
  - Argumentos: Especifican el objetivo de ejecución.
- **Manual de Comandos**: Uso del comando `man` para consultar funciones, opciones y argumentos de otros comandos.

### Comandos Básicos de Navegación y Manipulación
- **`pwd`**: Muestra la ruta del directorio actual.
- **`ls`**: Lista contenidos del directorio actual, con opciones para mostrar archivos ocultos (`-a`) y detalles (`-l`).
- **`cd`**: Cambia al directorio especificado.

### Comandos de Control de Flujo
- **`;`**: Separa comandos que se ejecutan secuencialmente.
- **`&&`**: Separa comandos, donde el segundo se ejecuta solo si el primero es exitoso.
- **`&`**: Ejecuta un comando en el fondo, permitiendo continuar con más comandos sin esperar.

### Obtención de Ayuda
- **`man`**: Muestra el manual del comando especificado.
- **`-h` o `--help`**: Muestra ayuda sobre un comando específico.

### Ver y Editar Archivos
- **`head` y `tail`**: Muestran las primeras o últimas líneas de un archivo, respectivamente.
- **`cat`**: Concatena y muestra el contenido de uno o más archivos.
- **`less`**: Permite la navegación interactiva dentro de un archivo de texto.
- **`nano`**: Editor de texto en consola, ideal para modificaciones rápidas.

### Redirección y Tuberías
- **`echo`**: Imprime texto en la terminal.
- **`>`**: Redirige la salida de un comando a un archivo, sobrescribiendo el contenido.
- **`|`**: Pasa la salida de un comando como entrada a otro.

### Gestión de Archivos y Directorios
- **`touch`**: Crea un nuevo archivo vacío o actualiza la fecha de uno existente.
- **`mkdir`**: Crea un nuevo directorio.
- **`rm` y `rmdir`**: Eliminan archivos y directorios, con opciones para eliminación recursiva (`-r`) y protección contra borrado accidental (`-i`).

### Enlaces de Archivos
- **`ln`**: Crea enlaces duros y simbólicos a archivos.
  - **Hard link**: Referencia directa a la misma ubicación de memoria del archivo original.
  - **Symbolic link**: Referencia indirecta mediante una ruta al archivo original.

### Herramientas de Monitorización
- **`df` y `du`**: Muestran información sobre el uso de espacio en disco.
- **`ps`, `top`, `htop`**: Proporcionan detalles sobre los procesos en ejecución.
- **`nohup` y `kill`**: Utilidades para manejar la ejecución de procesos en segundo plano y terminar procesos respectivamente.
