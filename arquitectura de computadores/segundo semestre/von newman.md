# Arquitectura de Von Neumann

La arquitectura de Von Neumann surgió después de la creación de la máquina ENIAC en 1946, la cual era muy grande, pesada, utilizaba kilómetros de cables y su programación era tediosa y compleja.

## Concepto revolucionario

El aporte clave de Von Neumann fue **el almacenamiento de programas en la misma memoria que los datos**, lo que permitió una mayor rapidez y eliminó la necesidad de múltiples conexiones físicas entre componentes. Esta idea sentó las bases para el diseño de las computadoras modernas.

---

## Componentes principales

### 1. Unidad de memoria principal

- Memoria compartida que almacena **datos e instrucciones**.
- Dividida en **celdas con direcciones únicas**.
- Acceso rápido y secuencial.

### 2. Unidad de procesamiento central (CPU)

Encargada de **ejecutar instrucciones**, **controlar la transferencia de datos** entre la memoria y los dispositivos de E/S, y responder a sus peticiones.

Se divide en dos unidades:

- **Unidad Aritmético-Lógica (ALU)**: 
  - Realiza operaciones aritméticas y lógicas con datos binarios.
  - Contiene registros como el **acumulador**, **registros temporales** y **registros de estado**.

- **Unidad de Control (UC)**:
  - Dirige el flujo de ejecución del programa.
  - Controla la **búsqueda**, **decodificación** y **ejecución** de las instrucciones.

### 3. Unidad de entrada/salida (E/S)

- Conecta la CPU con dispositivos externos como el **teclado**, **monitor** e **impresora**.
- Está dirigida por la Unidad de Control para permitir la entrada y salida de datos.

### 4. Buses de interconexión

- Líneas que **conectan y transmiten información** entre las distintas unidades de la computadora.

---

## Formato de datos en la IAS (Institute for Advanced Study)

- En la memoria, cada palabra tiene **40 bits**.
- Se pueden almacenar **dos instrucciones** por palabra: una en los 20 bits de la izquierda y otra en los 20 de la derecha.

**Formato de instrucción:**

- Bits 0–7: **CODOP** (código de operación).
- Bits 8–19: **Campo de dirección** (indica la posición del dato que se utilizará, no confundir con la dirección de memoria en sí).

**Palabras numéricas:**

- El primer bit indica el **signo** (0 = positivo, 1 = negativo).
- Los 39 bits restantes representan el número en binario (sistema decimal codificado).

---

## Flujo de datos

1. Instrucciones y datos se cargan desde la memoria al **MBR** (Memory Buffer Register).
2. El MBR transfiere información a la **unidad de control**.
3. La unidad de control **decodifica y ejecuta** las instrucciones.
4. La **ALU** realiza los cálculos necesarios.
5. Los resultados se almacenan en registros o se devuelven a la memoria.

---

## Ventajas

- **Flexibilidad**: se pueden cambiar los programas sin modificar el hardware.
- **Eficiencia**: se utiliza la misma memoria para datos e instrucciones.
- **Simplicidad**: diseño claro y fácil de implementar.
- **Universalidad**: es la base de la mayoría de las computadoras modernas.

---

## Limitaciones

- **Cuello de botella de Von Neumann**: la CPU y la memoria comparten un solo bus, lo que limita la velocidad.
- **Vulnerabilidad**: como datos e instrucciones comparten la misma memoria, un programa malicioso podría alterar el funcionamiento del sistema.

---

## Impacto en la computación moderna

- Es el **fundamento de las computadoras actuales**.
- Base para el desarrollo de **lenguajes de programación de alto nivel**.
- Inspiró arquitecturas más avanzadas como la **arquitectura Harvard**.
- Sigue influyendo en el diseño de **procesadores y sistemas informáticos** modernos.
