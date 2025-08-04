# Unidad de Memoria

La **unidad de memoria** es un conjunto de celdas de almacenamiento de datos o instrucciones. El sistema de memoria se refiere al conjunto de dispositivos y algoritmos de Hardware/Software (H/S) asociados al control de la memoria y otros circuitos que permiten ingresar y sacar información dentro de la memoria. Las funciones elementales de la memoria son la **lectura** y la **escritura** de datos.

La memoria también se puede considerar como un conjunto de **palabras** (registros), en cada una de ellas se puede almacenar un conjunto de **bits**. Un **registro** es un conjunto de bits posicionados uno a la par de otro, que tiene un significado o función específica, por eso se denomina **palabra**. Fuera de la memoria también existen registros, pero específicamente en la memoria se llaman **palabras**.

La **arquitectura de la computadora** debe estar definida, ya que nos indica la cantidad de bits que tiene la memoria, lo que es crucial para resolver el direccionamiento y la capacidad de operación de la misma.

## Clasificación Funcional

### Memoria Interna
Constituida por los registros internos de la **CPU**.

### Memoria Central (o Principal)
Almacena programas y datos, es relativamente **grande**, **rápida**, y es **accedida directamente** por la CPU a través de un **bus**.

### Memoria Secundaria
Se usa para el almacenamiento de programas del sistema y grandes archivos. Su capacidad es mucho mayor que las anteriores, pero es más lenta, y el acceso por parte de la CPU es indirecto.

## Parámetros Generales

| **Parámetro**                   | **Descripción**                                                                                                                                                                                                                                                                                                                                                      |     |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| **Unidad de almacenamiento**    | El bit, aunque comúnmente se usa el **byte** como unidad para almacenar información.                                                                                                                                                                                                                                                                                 |     |
| **Capacidad de almacenamiento** | Es la cantidad de bits que puede almacenarse, organizados en **palabras**.                                                                                                                                                                                                                                                                                           |     |
| **Tiempo de acceso (ta)**       | Es el tiempo que se tarda en leer o escribir una palabra en la memoria desde que se direcciona. La velocidad de acceso se mide en **palabras/segundo**.                                                                                                                                                                                                              |     |
| **Latencia CAS**                | Tiempo de acceso a la columna de la memoria, el retraso entre una solicitud de datos y el momento en que los datos empiezan a estar disponibles.                                                                                                                                                                                                                     |     |
| **Tipo de acceso**              | - **Acceso aleatorio**: El tiempo de acceso es similar para cualquier posición. <br> - **Acceso serie**: El tiempo de acceso depende de la posición.                                                                                                                                                                                                                 |     |
| **Tiempo de ciclo (tc)**        | Indica el mínimo tiempo entre dos accesos sucesivos a la memoria. El ancho de banda se define como la inversa de **tc**.                                                                                                                                                                                                                                             |     |
| **Medio físico**                | Electrónicas (semiconductores), magnéticas y ópticas (láser).                                                                                                                                                                                                                                                                                                        |     |
| **Estabilidad**                 | - **Volatilidad**: El contenido de la memoria se pierde cuando se suspende la alimentación eléctrica. <br> - **Almacenamiento dinámico**: El bit se almacena en un transistor MOS y pierde información cuando el capacitor se descarga. Requiere refresco periódico. <br> - **Lectura destructiva (DRO)**: La información se pierde al leerla y debe ser restaurada. |     |

## Memorias Electrónicas

### RAM (Random Access Memory)
La **RAM** significa **memoria de acceso aleatorio**, lo que significa que se puede acceder directamente a cualquier posición de memoria sin importar el orden de almacenamiento. La lectura o escritura de un dato en RAM es independiente de la posición de la memoria.

Dentro de la memoria RAM se encuentra la **ROM** (Read-Only Memory), aunque tiene características diferentes de la RAM, siendo solo un derivado de ella.

# Memoria de Escritura/Lectura

La **memoria de escritura/lectura** es una memoria activa, **volátil**, que permite almacenar de manera temporal datos y programas mientras el computador está encendido. La información se borra cuando se pierde la conexión eléctrica.

Es un espacio donde se depositan los códigos binarios de los programas del usuario en ejecución, los cuales son procesados para realizar cómputos. Su función principal es almacenar y devolver datos de manera temporal y sincronizada. Los programas residentes son aquellos que el usuario no sabe que están en ejecución.

## Capacidad y Canales de Comunicación

La capacidad y los canales de comunicación utilizados por la memoria son:

- **Single Channel**: Solo un canal de comunicación con el controlador de memoria.
- **Dual Channel**: Utiliza dos canales para duplicar la tasa de transferencia de datos.
- **Quad Channel**: Utiliza cuatro canales para un mayor ancho de banda.

## Tipos de Memoria RAM

### RAM Estática (Static RAM)
Es una memoria basada en circuitos integrados que posee un tiempo de acceso fijo a cualquier dato. No necesita ser reescrita cada cierto tiempo, lo que la hace más rápida que la RAM dinámica, pero también más costosa. Se utiliza en **memorias caché** o **registros**.

### RAM Dinámica (Dynamic RAM)
Es una memoria más lenta pero más económica, usada como memoria principal en los computadores para la ejecución de programas y almacenamiento de datos.

### Evolución de la Memoria RAM
- **Años 80**: **SDRAM** (Single Data Rate Synchronous DRAM), que operaba a la misma velocidad que el bus frontal. Actualmente ya no se usa mucho.
- **Años 90**: **DDR SDRAM** (Double Data Rate SDRAM), con versiones DDR2, DDR3, DDR4 y DDR5 (la mejor). Las diferencias entre estas versiones incluyen:
  - La variación en el **orificio** donde deben calzar en las ranuras de expansión.
  - Se **duplica la tasa de transferencia** de datos.
  - Se **reduce el consumo de energía**.

#### Tipos de Módulos de Memoria

| **Computadora**                | **Tipo de Módulo**             | **Número de Pines**         |
|---------------------------------|--------------------------------|-----------------------------|
| **Escritorios**                 | DIMM (Dual In-line Memory Module) | 168, 184, 240, 288          |
| **Portátiles/Laptops**          | SODIMM (Small Outline DIMM)    | -                           |

## Memoria de Solo Lectura (ROM)

La **ROM** es una memoria **pasiva**, **no volátil**, que contiene datos como **firmware** y no se puede actualizar. Es más lenta que la RAM y almacena información de manera permanente, como programas para la puesta en marcha del computador (cargar el sistema operativo, chequeo de hardware). Además, la computadora utiliza una pequeña memoria para almacenar la **BIOS** (Basic Input Output System) en una memoria **flash**.

### Tipos de Memoria ROM
- **ROM**: Grabados una vez por el fabricante.
- **PROM**: Grabado una vez por el usuario.
- **EPROM**: Se graban varias veces por el usuario. El borrado se realiza con luz ultravioleta.
- **EEPROM**: Se graban varias veces por el usuario. El borrado se realiza eléctricamente, posición por posición.
- **FLASH**: Se graban varias veces por el usuario. El borrado se realiza eléctricamente de una sola vez.

### Celda Elemental
Una celda elemental es un **biestable asíncrono** que permite almacenar un bit durante un periodo de tiempo. Se arma una estructura dentro de la celda para realizar lectura y escritura de datos, sirviendo como base para construir una memoria. Es importante evitar indeterminaciones en este proceso. El tipo de celda depende de la clase de memoria y la tecnología utilizada.

## Jerarquía de Memoria

La **jerarquía de memoria** establece que el nivel más bajo (memoria secundaria) tiene una mayor capacidad de almacenamiento, pero es más lento. En la cúspide (memoria caché y registros) se encuentra la memoria más rápida, pero con una menor capacidad de almacenamiento. 

A medida que aumenta el tipo de acceso, también aumenta el **costo de la transmisión por bit**.

# Memoria Principal

La **memoria principal** es el lugar donde se almacenan los datos o instrucciones que están siendo utilizados actualmente por el procesador. Estos datos se almacenan en **patrones binarios** en un circuito electrónico integrado, generalmente utilizando **memoria DRAM**.

Para que la memoria principal funcione correctamente, debe estar conectada con los demás componentes del computador a través del **bus de memoria**. La ruta de comunicación entre la memoria y la **CPU** se conoce como **puente norte del chipset** (Front-side Bus, **FSB**).

## Organización Interna de las Memorias RAM

### Memoria 2D

En una **memoria 2D**, la memoria se organiza en una matriz de dos dimensiones y se accede a ella mediante una sola línea de selección. Este tipo de organización es comúnmente utilizado en memorias de pequeña capacidad.

- **Líneas de direccionamiento**: $2^m$, donde **m** es el número de bits utilizados para el direccionamiento.

### Memoria 3D

En una **memoria 3D**, la memoria se accede mediante dos líneas de selección, lo que permite seleccionar la celda de memoria activando ambas líneas. Esta organización ayuda a reducir el tamaño de los **decodificadores** y es más eficiente en comparación con la organización 2D.

- **Líneas de direccionamiento**:  $2 \times 2^{\left(m/2\right)}$, donde **m** es el número de bits utilizados para el direccionamiento.

# Memorias de Lectura/Escritura Estáticas (SRAM)

## Organización y Estructura

- Organización en 2D: celdas dispuestas en forma de matriz (filas y columnas).
- Celda elemental basada en un **flip-flop** que almacena 1 bit.
- Modularización: se reutiliza una celda básica en toda la matriz.
- Cada cuadro representa una celda básica.

## Funcionamiento de Lectura y Escritura

| Operación | L/E | O/E | Descripción                                                       |     |
| --------- | --- | --- | ----------------------------------------------------------------- | --- |
| Lectura   | 1   | 0   | Entrada bloqueada, salida activada a través del buffer triestado. |     |
| Escritura | 0   | 1   | Entrada activada, dato escrito en la celda seleccionada.          |     |
| Reposo    | 1   | 1   | Alta impedancia. No lectura ni escritura.                         |     |
| Prohibido | 0   | 0   | **Conflicto lógico**, puede dañar el bus.                         |     |

### Estado de Reposo
- Cuando `L/E = 1` y `O/E = 1`, no se realiza ninguna operación.
- El buffer triestado entra en **alta impedancia** (Z), liberando el bus de datos.

### Conflicto lógico

- **No debe ocurrir:**  
  $$ L/E = 0 \quad \text{y} \quad O/E = 0 $$
  - Causa daño por conflicto entre entrada y salida activas al mismo tiempo.

## Señales de Control

| Señal     | Función |
|-----------|---------|
| `L/E`     | Controla si se escribe (`0`) o se lee (`1`). |
| `O/E`     | Habilita los buffers triestado para lectura (`0`). |
| `C/S’`    | Chip Select negado. Si está en `1`, la memoria está desactivada (alta impedancia). |
| `O/E’`    | Output Enable negado. Si está en `1`, los buffers de salida están deshabilitados. |

## Diseño de Memoria RAM

- Tamaño: **16 palabras** de **4 bits** cada una.
- Dirección: se usa un **decodificador 4x16**, con 4 bits de dirección:
  $$
  A_0, A_1, A_2, A_3
  $$
- Líneas de datos bidireccionales:
  $$
  I/O_0, I/O_1, I/O_2, I/O_3
  $$
- Uso de **buffers triestado** para permitir entrada y salida sobre las mismas líneas.

## Truco para Evitar Indeterminaciones en Flip-Flop SR

- Evitar la condición inválida:
  $$
  S = 1 \quad \text{y} \quad R = 1
  $$
- Regla para control:
  - Si entrada = 0 → conectar directamente a **R** (Reset).
  - Si entrada = 1 → conectar directamente a **S** (Set).
  - Para mantener estado:  
    $$
    S = 0 \quad \text{y} \quad R = 0
    $$

## Resumen de Estados

| Entrada | S | R | Estado del Flip-Flop |
|---------|---|---|----------------------|
| 0       | 0 | 1 | Reset (Q = 0)        |
| 1       | 1 | 0 | Set (Q = 1)          |
| —       | 0 | 0 | Mantiene estado      |
| —       | 1 | 1 | **Prohibido**        |
## Ciclo de Lectura/Escritura

### Proceso General

1. La CPU coloca la **dirección deseada** en el **bus de direcciones**.
2. Se utiliza el **bus de control** para indicar la operación deseada (lectura o escritura).
3. Según la operación:
   - **Lectura**: la memoria coloca el dato en el **bus de datos**.
   - **Escritura**: la CPU envía el dato a través del **bus de datos**.

### Requisitos de Señales

- La línea `CS'` (**Chip Select**) debe estar en `0` desde el inicio del proceso.
- Se debe garantizar sincronización entre:
  - Dirección aplicada.
  - Señales de control (`L/E`, `O/E`, etc.).
  - Transferencia de datos por el bus.

---

## Memorias de Lectura/Escritura Dinámicas (DRAM)

### Estructura de la Celda Básica

- Una **celda DRAM** está compuesta por:
  - Un **transistor MOS**.
  - Un **condensador** (capacidad parásita).

- Los datos se almacenan como **carga eléctrica** en el condensador.

### Necesidad de Refresco

- La carga se **disipa con el tiempo**, por lo que se requiere un **ciclo de refresco periódico**.
- El **refresco** implica:
  - **Lectura** del valor almacenado.
  - **Escritura automática** del mismo valor.

- Durante el refresco:
  - La **memoria no está disponible** para acceso normal.

- El proceso es gestionado por:
  - Un **controlador de DRAM**, que puede ser interno o externo.

### Organización de Direcciones

- Organización habitual: **3D** (matriz de filas y columnas).
- La dirección se divide:
  $$
  m \text{ bits de dirección} \Rightarrow \frac{m}{2} \text{ bits para fila (ROW)},\ \frac{m}{2} \text{ bits para columna (COLUMN)}
  $$

### Multiplexación Temporal

- Las **líneas de dirección están multiplexadas**:
  1. Se envían primero los bits de **fila**, cargados con la señal `RAS` (Row Address Strobe).
  2. Luego los bits de **columna**, cargados con la señal `CAS` (Column Address Strobe).

- Ventaja: se **reduce el número de líneas del bus de direcciones** a la mitad.

### Ejemplo de Dirección

- Para una matriz de $32 \times 32$, se necesitan $16$ bits de direccionamiento:

  $$
  \log_2(32 \times 32) = \log_2(1024) = 10 \Rightarrow 5 \text{ bits para fila, 5 bits para columna}
  $$

### Accesos Consecutivos

- Si se deben leer/escribir **direcciones consecutivas** y están en la **misma fila**, sólo es necesario:
  - **Cambiar la dirección de columna**.
  - Mantener la misma dirección de fila.
  - Esto optimiza el tiempo de acceso.

---


# Memorias de Lectura (ROM)

## Organización Interna

- La estructura interna de una **ROM** es similar a la de una memoria RAM, pero **solo permite lectura**.
- Se utilizan componentes como:
  - **Diodos** o **transistores**
  - Una **conexión física** representa un $1$
  - La **ausencia de conexión** representa un $0$
- La conexión de varias salidas a una misma línea implementa una función lógica **OR**.

## Capacidad

Una ROM puede organizarse como:

$$
2^n \times m
$$

Donde:

- $n$: número de **variables de entrada**.
- $m$: número de **funciones de salida**.

Esto significa que puede realizar cualquier función lógica **combinacional** de $n$ entradas y $m$ salidas.

## Ejemplo

Supongamos una ROM de:

$$
2^3 \times 4
$$

- Puede manejar **8 combinaciones** de entrada (porque $2^3 = 8$).
- Para cada combinación, entrega una palabra de **4 bits de salida**.
- Es capaz de implementar **4 funciones lógicas** de 3 variables de entrada.
---
# Memoria Auxiliar

La memoria auxiliar, también conocida como memoria secundaria o almacenamiento secundario, se refiere a los dispositivos que permiten almacenar datos de forma permanente o semipermanente, incluso cuando el computador está apagado. Estos dispositivos son esenciales para mantener la persistencia de la información, como documentos, programas, aplicaciones y sistemas operativos.

---

## Discos Magnéticos

Los discos magnéticos son dispositivos de almacenamiento que utilizan un medio magnetizado para almacenar datos digitalmente. El ejemplo más común es el disco duro (HDD).

- **Estructura**: Contienen platos circulares cubiertos de material magnético y un brazo mecánico con cabezales de lectura/escritura que giran a alta velocidad dentro de una caja metálica sellada para evitar el ingreso de partículas de polvo que puedan dañarlos.

- **Manejo seguro**: Es importante desconectar la corriente eléctrica, tocar la carcasa o usar una muñequera antiestática al manipularlos para evitar daños en la información.

- **Características**:
  - Admiten grandes volúmenes de información.
  - Son menos duraderos que otros dispositivos.
  - Consumen más energía y generan ruido debido a las partes móviles.
  - Pueden presentar cuellos de botella en la transferencia de datos.

- **Velocidad**: Se mide en revoluciones por minuto (RPM).

  | Tipo de dispositivo        | Velocidad (RPM) |
  |---------------------------|-----------------|
  | Portátiles                | 5400 o 7200     |
  | Computadoras de escritorio| 10,000 o más    |

- **Conexiones comunes**:
  - IDE (Integrated Drive Electronics)
  - SATA (Serial Advanced Technology Attachment)

---

## Memoria Flash

La memoria flash es un tipo de memoria de estado sólido que no tiene partes móviles y almacena datos mediante cargas eléctricas en celdas de memoria. Es capaz de ser programada, borrada y reescrita electrónicamente.

- **Ventajas**:
  - Mayor velocidad de lectura y escritura.
  - Menor consumo de energía y generación de calor.
  - Tamaño reducido y mayor resistencia a golpes.

- **Ejemplos**:
  - SSD (Solid State Drive)
  - Pendrives
  - Tarjetas de memoria

- **Tipos de memoria flash**:

  | Tipo | Uso común                           | Costo |
  |------|-------------------------------------|-------|
  | NAND | Almacenamiento general (SSD)        | Bajo  |
  | NOR  | Firmware (BIOS, UEFI, microcontroladores) | Alto  |

---

## Cinta Magnética

La cinta magnética es un medio de almacenamiento que utiliza una cinta recubierta con material magnético para almacenar datos de forma secuencial.

- **Características**:
  - Acceso secuencial a los datos.
  - Menor velocidad en comparación con otros dispositivos.
  - Utilizada principalmente para copias de seguridad y almacenamiento a largo plazo.

---

## Memoria Caché

La memoria caché es una memoria rápida y costosa que se sitúa entre la RAM y la CPU, acelerando la transferencia de datos entre ambos.

- **Funcionamiento**: Cuando la CPU necesita un dato, se copia un bloque de memoria desde la RAM a la caché, permitiendo que los datos siguientes se lean/escriban desde la caché, que es más rápida.

- **Ventajas**:
  - Mejora el desempeño del programa al permitir que se ejecute más rápido.
  - Reduce el tiempo de acceso a los datos más utilizados.

- **Ubicación**:
  - Puede estar ubicada dentro o fuera de la CPU.
  - Se sitúa entre la memoria principal y los registros de la CPU.

### Niveles de Caché

| Nivel | Ubicación             | Tamaño típico           | Velocidad |
|-------|-----------------------|-------------------------|-----------|
| L1    | Dentro del procesador | 64 kB (32 kB datos + 32 kB instrucciones) | Muy alta  |
| L2    | En el procesador      | 256 kB                  | Alta      |
| L3    | Fuera del procesador  | 12 MB                   | Media     |

- **Relaciones de tamaño**:

  $$
  \text{L2} = 8 \times \text{L1} \\
  \text{L3} = 16 \times \text{L2}
  $$

---

## Buses

Los buses son conductores eléctricos que transportan información entre los diversos componentes de un sistema informático.

- **Propósito**: Reducir el número de caminos necesarios para la comunicación entre componentes, llevando en un solo canal de datos todas las comunicaciones necesarias, evitando cuellos de botella.

- **Composición**: Están formados por cables de cobre o fibra óptica, pistas en circuitos impresos, resistencias, capacitores, resistores y circuitos integrados.

### Tipos de Buses

#### Bus de Datos

- **Función**: Es bidireccional y proporciona un camino para transmitir datos o instrucciones entre la CPU, la memoria y los dispositivos de E/S.

- **Dependencia**: Depende del tamaño de la palabra del procesador y la arquitectura general del sistema.

- **Ejemplo**:
  - Si se tiene un bus de datos de 32 bits y un procesador de 32 bits, puede transferir una palabra de 4 bytes (32 bits) en cada ciclo.
  - Si se tiene una palabra de 8 bytes, el procesador debe acceder al módulo de memoria dos veces por cada ciclo de instrucción.

#### Bus de Direcciones

- **Función**: Es unidireccional, ya que la información viaja desde la CPU a la memoria o dispositivos periféricos.

- **Uso**: Se utiliza para designar la fuente o el destino del dato situado en el bus de datos.

- **Capacidad de direccionamiento**:
  - En un sistema de 32 bits:

    $$
    2^{32} = 4\,294\,967\,296 \text{ direcciones} = 4\,\text{GB}
    $$

  - En un sistema de 64 bits, normalmente se usan 48 bits para direccionar:

    $$
    2^{48} = 281\,474\,976\,710\,656 \text{ direcciones} = 128\,\text{GB}
    $$

#### Bus de Control

- **Función**: Es bidireccional y se utiliza para controlar el acceso y el uso de las líneas de datos y de direcciones.

- **Composición**: Está formado por líneas independientes de entrada o salida a la CPU que se utilizan para controlar y sincronizar las operaciones que se realizan entre los distintos dispositivos, determinando cuál tiene más prioridad.

- **Uso**: Especifica la acción a realizar mediante señales de control.

---

