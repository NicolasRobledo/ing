# ¿Cómo funciona una computadora?

## Hardware y Software

- El **hardware** necesita recibir instrucciones claras para saber qué procesos realizar.  
- Estas instrucciones se definen a través de **programas de computación**, creados por programadores.

---

## Programas de computación

- Están formados por un conjunto de **instrucciones** escritas en lenguajes de programación como **C** o **Java**.  
- No son directamente comprensibles por el hardware de la computadora.

---

## Compilación

- **Compilar** significa traducir un programa a un conjunto de instrucciones entendibles por la computadora, es decir, a **lenguaje máquina**.

```
Archivo fuente (.c o .java) → Compilador → Archivo ejecutable (lenguaje máquina)
```

---

## Proceso de ejecución

1. El archivo fuente (por ejemplo, en C) está almacenado en el **disco duro**.  
2. El código fuente es **compilado** a un archivo ejecutable en **lenguaje máquina**.  
3. El ejecutable se **carga** desde el disco a la **memoria principal (RAM)**.  
4. El **procesador (CPU)** comienza a ejecutar las instrucciones.  
5. Los resultados se envían a un **dispositivo de salida** (por ejemplo, el monitor).

---
# Componentes de una computadora

Un computador hardware es un dispositivo electrónico que incluye una serie de componentes interconectados para realizar tareas específicas con la finalidad de permitirnos navegar por internet, crear un dibujo, entre otros. El software son los programas de computación que se ejecutan en este y controlan el hardware. Debe permitir el movimiento de los datos desde el exterior (entrada) o hacia el exterior (salida) y los individuos son capaces de controlar el computador construyendo las instrucciones que implementan las otras funcionalidades.

## Flujo de datos en la computadora

El flujo de datos en una computadora sigue el siguiente proceso:

| **Entrada**      | **Operaciones de procesamiento**  | **Salida**   |
|------------------|-----------------------------------|--------------|
| Datos del usuario (teclado, ratón, etc.) | Procesamiento por el CPU o unidad de procesamiento central | Resultados visibles para el usuario (pantalla, impresora, etc.) |

Este proceso permite que la computadora realice tareas específicas y entregue resultados a los usuarios.

Para representar el flujo de datos de manera formal, podemos utilizar una ecuación en LaTeX que lo describa:

$$
\text{Entrada} \rightarrow \text{Operaciones de procesamiento} \rightarrow \text{Salida}
$$
# Placa Madre

La **placa madre** es la pieza que une todos los elementos de un equipo de cómputo para que funcione en conjunto. Tiene elementos extraíbles como:

- **Memoria RAM**
- **Discos duros**
- **Discos de estado sólido**
- **Tarjeta de video**
- **Microprocesador**

Otros componentes vienen soldados por defecto, como:

## Componentes de la Placa Madre

| **Componente**                      | **Descripción**                                                                                                                                          |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Zócalos para el microprocesador**  | Elemento de sujeción del microprocesador a los buses de comunicación de la tarjeta madre.                                                                |
| **Sockets para memoria RAM**        | Elementos de sujeción de la memoria RAM a la comunicación de los núcleos del microprocesador.                                                             |
| **Sockets PCI Express**             | Elemento de sujeción para tarjetas de video, ethernet, y tarjetas de audio.                                                                                |
| **Chipset**                          | Circuito integrado que actúa como puente de comunicación entre algunos sockets PCIe, puertos USB, SATA, HDMI, VPORT, ethernet y el microprocesador.       |
| **Chip del BIOS**                   | Circuito de arranque del CPU que ejecuta el Sistema Operativo. Es el más importante, ya que detecta todos los dispositivos conectados. Incluye firmware. |

## Funcionamiento del BIOS

El **BIOS** (Basic Input/Output System) es el primer sistema que se ejecuta al encender la computadora. Su funcionamiento es el siguiente:

1. **Encendido**: Al presionar el botón de encendido, el **BIOS** activa la alimentación de toda la tarjeta madre.
2. **Verificación**: Luego, ejecuta el programa **POST** (Power-On Self-Test), que verifica los sistemas conectados.
3. **Acceso a configuración**: Si no recibe una directiva para acceder a la configuración interna, ejecuta el Sistema Operativo (S.O.).
4. **Batería**: El BIOS se mantiene activo incluso cuando la computadora está apagada, alimentado por una batería de reloj.

### Controladores de dispositivo

La placa base generalmente viene acompañada de un **CD** que contiene los controladores de dispositivo de cada uno de los componentes soportados.

## Velocidad del CPU

La velocidad del **CPU** es el número de instrucciones que puede procesar en un segundo bajo condiciones ideales. Se mide en **Hertz** (ciclos por segundo). Los procesadores más rápidos generan niveles altos de calor, lo que puede requerir sistemas de refrigeración más avanzados para mantener la temperatura bajo control.
