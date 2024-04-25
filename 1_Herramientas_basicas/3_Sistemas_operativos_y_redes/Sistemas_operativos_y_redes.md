# Sistemas Operativos y Redes

## Definición de Sistema Operativo
- **Función Principal**: Administra el hardware de una computadora y actúa como intermediario entre el usuario y el hardware.
- **Roles**:
  - Gestiona recursos hardware.
  - Proporciona bases para programas de aplicación.
  - Facilita la ejecución y gestión de aplicaciones.

## Arquitectura de un Sistema Operativo
- **Kernel**: Núcleo del sistema operativo.
  - **Funciones del Kernel**:
    - Gestión de procesos.
    - Gestión de memoria.
    - Acceso al sistema de archivos.
    - Comunicación con hardware a través de controladores.
  - **Interacción con el Usuario**: A través de un shell para comandos y/o una interfaz gráfica.

## Kernel

### Gestión de Procesos
- **Procesos**: Programas en ejecución que incluyen código, datos, estado del contador de programa, registros, etc.
- **Estados de un Proceso**:
  - **Nuevo**: Creación del proceso.
  - **Listo**: Esperando a ser asignado al procesador.
  - **Ejecutando**: Proceso en ejecución.
  - **Bloqueado**: Esperando por un evento (Ej: I/O).
  - **Terminado**: Finalización del proceso.
- **Multitarea**: Apariencia de ejecución simultánea de múltiples procesos.
- **Jerarquía de Procesos**: Procesos padres e hijos con gestión de recursos compartidos.

### Gestión de Memoria
- **Memoria Principal**: Dividida en segmentos, cada uno accesible sólo por su proceso designado.
- **Violaciones de Segmento**: Causadas por accesos no autorizados fuera del segmento asignado.
- **Memoria Virtual (Swap)**: Extensión de la RAM en el disco duro para manejar la sobrecarga de procesos.

### Multitarea y Planificación
- **Scheduler (Planificador)**: Administra el tiempo de CPU asignado a cada proceso.
- **Control de Interrupciones**: Gestión de las señales de hardware para coordinar tareas y manejo de dispositivos.

### Controladores de Dispositivos
- **Drivers**: Facilitan la interacción entre el sistema operativo y el hardware.
- **Función**: Traducen las necesidades del software al hardware y viceversa.

## Seguridad y Modos de Operación
- **Modo Supervisor**: Acceso ilimitado al hardware, utilizado por el BIOS y el kernel.
- **Modo Protegido**: Restringe el acceso directo al hardware para procesos de usuario.
- **Anillos de Protección**: Jerarquías de privilegios dentro del sistema que aseguran la seguridad operativa.

## Familias de Sistemas Operativos

### Unix
- **Origen**: Desarrollado en 1969 por empleados de AT&T en Bell Labs.
- **Filosofía**: Código simple, corto, claro, modular y extensible.
- **Características**:
  - Sistema de ficheros jerárquico.
  - Uso de pequeños programas en serie.
  - Trata los dispositivos como ficheros.
  - Almacenamiento de datos en ficheros de texto.

### Familia Unix

1. **Linux**:
   - **Descripción**: Combinación de proyectos GNU y el kernel Linux.
   - **Origen**: Proyecto GNU iniciado en 1983 por Richard Stallman; Kernel Linux iniciado en 1991 por Linus Torvalds.
   - **Características**: Software libre, código fuente abierto y modificable.

2. **Android**:
   - **Descripción**: Basado en núcleo Linux, diseñado para dispositivos táctiles.
   - **Dominio**: Sistema operativo móvil más utilizado mundialmente.

3. **BSD**:
   - **Origen**: Derivado de Unix, desarrollado por la Universidad de California en Berkeley.
   - **Descendientes**: SunOS, FreeBSD, NetBSD, OpenBSD, y Mac OS X.

4. **macOS**:
   - **Descripción**: Desarrollado por Apple, utilizado en computadoras Mac.
   - **Base**: Desarrollado a partir de BSD.
   - **Uso**: Popular entre diseñadores gráficos y músicos.

5. **iOS**:
   - **Descripción**: Desarrollado por Apple para iPhone, iPad, y iPod touch.
   - **Base**: Deriva de macOS y, por ende, de BSD.

### Windows
- **Origen**: Introducido por Microsoft en 1985 como un complemento para MS-DOS.
- **Dominio**: Mayor cuota de mercado en computadoras personales y servidores.
- **Evolución**: Desde una simple GUI hasta sistemas operativos completos para diferentes dispositivos.

## Conceptos Clave de Redes de Telecomunicaciones

- **Definición**: Redes que permiten la comunicación a distancia entre equipos autónomos mediante diversos medios.
- **Internet**:
  - **Origen**: ARPANET en 1969.
  - **Servicios**: SMTP (email), FTP (transferencia de archivos), IRC (chat), entre otros.

## Modelo OSI

- **Desarrollo**: Por la ISO en 1984 para estandarizar la comunicación en redes informáticas.
- **Capas**:
  1. **Física**: Especificaciones mecánicas y eléctricas para la transmisión física.
  2. **Enlace de Datos**: Gestión de la comunicación directa entre dispositivos de red, control de errores y flujos.
  3. **Red**: Determinación de la ruta óptima y lógica para los datos entre redes.
  4. **Transporte**: Seguridad en la transferencia de datos entre puntos finales.
  5. **Sesión**: Gestión de sesiones entre aplicaciones.
  6. **Presentación**: Traducción de datos para la aplicación.
  7. **Aplicación**: Interfaz para aplicaciones de red.

- **Funciones**: Proporciona un marco para crear y estandarizar protocolos de red en siete capas.
- **Diferencias con TCP/IP**: OSI es un modelo teórico mientras que TCP/IP es una suite de protocolos práctica usada en Internet.

## Capa de Transporte: TCP vs UDP

### TCP (Protocolo de Control de Transmisión)
- **Orientado a la conexión**: Requiere establecimiento de conexión antes de la transmisión de datos mediante un handshake de tres vías.
- **Fiabilidad**: Garantiza la entrega de datos sin errores, en orden y sin duplicados. Si hay pérdida de paquetes, TCP los retransmite.
- **Control de flujo**: Utiliza una ventana deslizante para controlar la cantidad de datos que se envían sin recibir una confirmación.
- **Control de congestión**: Reduce la tasa de envío de datos cuando detecta congestión en la red.
- **Usos comunes**: HTTP, HTTPS, FTP, SMTP, SSH, entre otros, que requieren fiabilidad en la entrega de datos.

**Características técnicas**:
- **Numeración de segmentos**: Permite la reordenación de segmentos y la detección de duplicados.
- **Checksums**: Para verificar la integridad de los datos.
- **ACKs (Acuses de recibo)**: Confirman la recepción de los segmentos.
- **Puertos**: Facilitan la multiplexación de datos de múltiples aplicaciones en un mismo host.

### UDP (Protocolo de Datagramas de Usuario)
- **No orientado a la conexión**: No requiere establecimiento de conexión previo, lo que reduce la latencia.
- **No confiable**: No garantiza la entrega de datos; no hay retransmisión de datagramas perdidos.
- **Sin control de flujo ni de congestión**: No ajusta la tasa de envío de datos basándose en la capacidad del receptor o en las condiciones de la red.
- **Usos comunes**: DNS, DHCP, aplicaciones de streaming de audio y video, donde la velocidad es más crítica que la fiabilidad.

- **Características técnicas**:
  - **Cabecera ligera**: Solo 8 bytes, lo que reduce el overhead y mejora la eficiencia en redes de alta velocidad.
  - **Checksum opcional**: Para la verificación de errores tanto en la cabecera como en los datos.
  - **Puertos**: Similar a TCP, facilita la identificación de la aplicación destino.

### Comparación de TCP y UDP
- **TCP** es ideal para aplicaciones que necesitan alta fiabilidad y donde la entrega correcta y ordenada de los datos es crucial.
- **UDP** es mejor para aplicaciones que necesitan velocidad y eficiencia, y pueden tolerar alguna pérdida de datos, como en el streaming en tiempo real o juegos en línea.

### Importancia en la Capa de Transporte
- La capa de transporte es crítica porque proporciona la funcionalidad de comunicación entre aplicaciones en diferentes sistemas. Administra la entrega de datos de aplicación a aplicación y es fundamental para determinar cómo se transmiten los datos a través de la red, ajustando la comunicación a las necesidades de la aplicación y las condiciones de la red.
