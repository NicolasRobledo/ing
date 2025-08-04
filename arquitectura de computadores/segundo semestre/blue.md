# Máquina Elemental – BLUE

## Características Generales

- Usa sistema binario y complemento a dos.
- Memoria de $4096 \times 16$ (4096 posiciones de memoria de 16 bits cada una).
- Usa punto fijo por hardware.
- Datos de 16 bits (15 bits de magnitud y 1 bit de signo).
- Instrucciones de longitud fija de 16 bits.
- Bus de datos: 16 bits.
- Bus de direcciones: 12 bits.

## Panel de Control

- Pulsador de ARRANQUE (Start)
- Pulsador de PARADA (Stop)
- Pulsador de CARGAR PC (Load PC)
- Pulsador de DEPOSITAR (Deposite): Almacenar en una dirección de memoria específica.
- Pulsador de EXAMINAR (Examine)
- Pulsador de RESET (Reset)
- 16 llaves de 3 posiciones
- 16 LEDs (luces)

Estos pulsadores permiten la interacción directa con la máquina para operaciones específicas.

## Formato de Instrucción

- Longitud fija: 16 bits
- Código de operación: 4 bits → $2^4 = 16$ instrucciones
- Campo de dirección: 12 bits

$$
\text{Instrucción} = \underbrace{\text{CODOP}}_{4\ bits} \ +\ \underbrace{\text{Dirección (X)}}_{12\ bits}
$$

## Registros

### ALU (Unidad Aritmético-Lógica)

| Registro | Función |
|----------|---------|
| **AC** (Acumulador) | Almacena resultados temporales |
| **MQ** (Multiplicador) | Operaciones aritmético-lógicas |
| **MBR** (Memory Buffer Register) | Intermediario entre memoria y bus de datos |

### UC (Unidad de Control)

| Registro | Función |
|----------|---------|
| **IR** (Instruction Register) | Guarda el código de operación (CODOP) |
| **IBR** (Instruction Buffer Register) | Guarda parte derecha de la instrucción (siguiente instrucción) |
| **PC** (Program Counter) | Lleva la secuencia de instrucciones a ejecutar |
| **MAR** (Memory Address Register) | Guarda direcciones de datos/instrucciones desde el bus de direcciones |

## Instrucciones

| N | Nombre | Mnemónico | Descripción |
|---|--------|-----------|-------------|
| 0 | Halt (parar) | `HLT X` | Detiene la CPU hasta una intervención externa. |
| 1 | Add (sumar) | `ADD X` | Suma en complemento a dos el valor de la memoria `X` al acumulador. |
| 2 | OR-exclusiva | `XOR X` | OR exclusiva bit a bit con la dirección `X`. |
| 3 | AND | `AND X` | AND bit a bit con la dirección `X`. |
| 4 | OR | `IOR X` | OR bit a bit con la dirección `X`. |
| 5 | NOT (complemento A1) | `NOT X` | Complemento lógico de cada bit en el acumulador. |
| 6 | Cargar AC | `LDA X` | Carga el contenido de la memoria `X` al acumulador. |
| 7 | Almacenar AC | `STA X` | Guarda el acumulador en la dirección de memoria `X`. |
| 8 | Salto a subrutina | `SRJ X` | Salta a una subrutina. |
| 9 | Salto condicional | `JMA X` | Salta si el bit de signo del acumulador es 1. |
| 10 | Salto incondicional | `JMP X` | Copia `X` en `PC` para ejecutar otra parte del programa. |
| 11 | Entrada de datos | `INP X` | Recibe un byte desde el dispositivo externo y lo coloca en el acumulador. |
| 12 | Salida de datos | `OUT X` | Envía los 8 bits más significativos del acumulador al dispositivo externo. |
| 13 | Rotación de bits | `RAL X` | Rota los bits del acumulador a la izquierda. |
| 14 | Copiar llaves | `CSA X` | Copia el número de las llaves al acumulador. |
| 15 | No operación | `NOP X` | No hace nada. |

## Ejecución de un Programa

El ciclo de ejecución consta de:

1. Leer una instrucción desde memoria.
2. Identificar o decodificar la instrucción.
3. Comprobar si requiere acceso a memoria o E/S.
4. Ejecutar la instrucción.
5. Repetir desde el paso 1 hasta completar el programa.

