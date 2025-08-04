# Sistemas Digitales

Es un conjunto de elementos **binarios** relacionados entre sí de alguna manera. En un sistema digital se distinguen dos tipos de variables:
- **Variables de entrada**
- **Variables de salida** (dependen de las de entrada).

Se divide en dos categorías principales:

## 1. Sistemas **Combinacionales**
- Dependen de las **combinaciones de entradas y salidas**, donde estas son las funciones.
- Las salidas son afectadas **únicamente por las entradas presentes**.
- **Ejemplos**: Codificadores, decodificadores, MUX, DEMUX, sumadores, restadores, ROM.

## 2. Sistemas **Secuenciales**
- Dependen de una **secuencia establecida en la tabla lógica**.
- Pueden tener salida y entrada, pero incluyen **retroalimentación hacia elementos de memoria** que permiten guardar datos.
- **Ejemplos**: Flip-flops, registros, contadores, memorias RAM.
- Operan con **tiempos evolutivos**: trabajan con frecuencias que generan variaciones en el tiempo, permitiendo operaciones dentro de un cómputo.

---

### Conceptos Clave
- **Retroalimentación**: Permite que el circuito tenga valores predefinidos y "recuerde" un valor en términos de tiempo. Esencial para cómputos secuenciales y almacenamiento de **1 bit**.
  
- **Reutilizar componentes/modularizar**: Consiste en tomar una función específica e integrarla en un chip independiente para simplificar diseños complejos.
- # Circuitos Combinacionales: Semisumador y Sumador Completo

## **Semisumador (Half-Adder)**
![[Half_Adder.png]] 

- **Definición**: Circuito combinacional para sumar **2 bits** (A y B).
- **Salidas**:
  - **$\Sigma$ (Suma)**: Resultado sin acarreo → $\Sigma = A \oplus B$ (compuerta **XOR**).
  - **$C_{out}$ (Acarreo)**: Acarreo generado → $C_{out} = A \cdot B$ (compuerta **AND**).
  
### **Tabla de Verdad del Semisumador**
| A | B | $\Sigma$ | $C_{out}$ |
|---|---|----------|-----------|
| 0 | 0 |    0     |     0     |
| 0 | 1 |    1     |     0     |
| 1 | 0 |    1     |     0     |
| 1 | 1 |    0     |     1     |

**Características**:
- Si **A = B** → $\Sigma = 0$ (por XOR).
- $C_{out} = 1$ **solo si A y B son 1**.

---

## **Sumador Completo (Full-Adder)**
![[fullAdder.png]]
- **Definición**: Circuito combinacional para sumar **3 bits** (A, B, $C_{in}$).
- **Salidas**:
  - **$\Sigma$ (Suma)**: $\Sigma = A \oplus B \oplus C_{in}$.
  - **$C_{out}$ (Acarreo)**: $C_{out} = (A \cdot B) + (C_{in} \cdot (A \oplus B))$.

### **Tabla de Verdad del Sumador Completo**
| A | B | $C_{in}$ | $\Sigma$ | $C_{out}$ |
|---|---|---------|----------|-----------|
| 0 | 0 |    0    |    0     |     0     |
| 0 | 0 |    1    |    1     |     0     |
| 0 | 1 |    0    |    1     |     0     |
| 0 | 1 |    1    |    0     |     1     |
| 1 | 0 |    0    |    1     |     0     |
| 1 | 0 |    1    |    0     |     1     |
| 1 | 1 |    0    |    0     |     1     |
| 1 | 1 |    1    |    1     |     1     |

**Funcionamiento**:
- **$C_{in}$**: Acarreo de una etapa anterior (ej: salida de otro semisumador).
- **Expresión general**: $A + B + C_{in} = \Sigma + 2 \cdot C_{out}$ *(2 representa el peso binario del acarreo)*.

---



# Memorias (Biestables)

## Biestables
- **Definición**: Secuenciales con dos estados estables donde las variables internas pueden adoptar dos estados permanentes hasta que cambien las entradas.
- **Característica clave**: Mantienen su estado hasta ser modificados por un pulso de reloj (en síncronos) o cambios directos en entradas (en asíncronos).

---

### Tipos según sincronismo
#### Asíncronos
- Las entradas actúan directamente sobre el biestable (ej: flip-flop sin reloj).
- **Ventaja**: Mayor velocidad de respuesta.

#### Síncronos
- Incluyen una entrada adicional de señal de reloj (CP).
- **Subtipos**:
  1. **Activados por nivel**:  
     La tabla de verdad solo es válida durante el nivel activo del reloj (ej: cresta positiva).
  
  2. **Maestro-esclavo**:  
     Usa dos biestables interconectados: uno actúa con CP=0 y otro con CP=1.
  
  3. **Activados por flancos**:  
     Cambian de estado únicamente en la transición del reloj (ej: de bajo a alto).

---

## Flip Flop RS sin reloj
### Características
- **Entradas**:  
  - `R` (Reset): Limpia el bit (estado 0).  
  - `S` (Set): Fija el bit (estado 1).  

- **Implementaciones**:
  - **Con compuertas NAND**:  
    - `R=1 ∧ S=1` → Mantiene estado anterior.  
    - `R=0 ∧ S=0` → Indeterminación.  

  - **Con compuertas NOR**:  
    - `R=1 ∧ S=1` → Indeterminación.  
    - `R=0 ∧ S=0` → Mantiene estado anterior (EDA).  

- **Recomendación de uso**:  
  Inicializar siempre con:  
  - `S=1 ∧ R=0` (establecer a 1), o  
  - `S=0 ∧ R=1` (resetear a 0).
![[flip-flop-nand.png]] ![[flipflop-nor.png]]
$$
\begin{array}{|c|c|c|c|}
\hline
\mathbf{S} & \mathbf{R} & \mathbf{Q} & \mathbf{\overline{Q}} \\
\hline
1 & 0 & 1 & 0 \, \text{(Set)} \\
1 & 1 & \text{Mantiene} & \text{Mantiene} \\
0 & 1 & 0 & 1 \, \text{(Reset)} \\
0 & 0 & \text{Ind} & \text{(Inválido)} \\
\hline
\end{array}
$$

---
# Flip-Flops

## Flip-Flop RS Asíncrono (NAND)
### Tabla de Verdad
$$
\begin{array}{|c|c|c|c|}
\hline
\mathbf{S} & \mathbf{R} & \mathbf{Q} & \mathbf{\overline{Q}} \\
\hline
1 & 0 & 1 & 0 \, \text{(Set)} \\
1 & 1 & \text{Mantiene} & \text{Mantiene} \\
0 & 1 & 0 & 1 \, \text{(Reset)} \\
0 & 0 & \text{Ind} & \text{(Prohibido)} \\
\hline
\end{array}
$$

### Ecuación
$$ Q(t+1) = S + \overline{R}Q(t) $$

---

## Flip-Flop RS Síncrono (con Reloj)
### Tabla de Verdad (CP=1)
$$
\begin{array}{|c|c|c|c|}
\hline
\mathbf{S} & \mathbf{R} & \mathbf{Q(t)} & \mathbf{Q(t+1)} \\
\hline
0 & 0 & 0 & 0 \\
0 & 0 & 1 & 1 \\
0 & 1 & 0 & 0 \\
0 & 1 & 1 & 0 \\
1 & 0 & 0 & 1 \\
1 & 0 & 1 & 1 \\
1 & 1 & X & \text{Ind} \\
\hline
\end{array}
$$

---

## Flip-Flop D
### Tabla de Verdad
$$
\begin{array}{|c|c|c|}
\hline
\mathbf{D} & \mathbf{Q(t)} & \mathbf{Q(t+1)} \\
\hline
0 & 0 & 0 \\
0 & 1 & 0 \\
1 & 0 & 1 \\
1 & 1 & 1 \\
\hline
\end{array}
$$

**Función**:  
$$ Q(t+1) = D $$

---

## Flip-Flop JK
### Tabla de Verdad
$$
\begin{array}{|c|c|c|c|}
\hline
\mathbf{J} & \mathbf{K} & \mathbf{Q(t)} & \mathbf{Q(t+1)} \\
\hline
0 & 0 & X & \text{Mantiene} \\
0 & 1 & X & 0 \\
1 & 0 & X & 1 \\
1 & 1 & X & \overline{Q(t)} \\
\hline
\end{array}
$$

**Ecuación**:  
$$ Q(t+1) = J\overline{Q(t)} + \overline{K}Q(t) $$

---

## Flip-Flop T
### Tabla de Verdad
$$
\begin{array}{|c|c|c|}
\hline
\mathbf{T} & \mathbf{Q(t)} & \mathbf{Q(t+1)} \\
\hline
0 & 0 & 0 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
1 & 1 & 0 \\
\hline
\end{array}
$$

**Función**:  
$$ Q(t+1) = T \oplus Q(t) $$

---

## Mapa de Karnaugh (Ejemplo RS)
$$
\begin{array}{|c|c|c|c|c|}
\hline
 & \overline{R}\overline{S} & \overline{R}S & R S & R\overline{S} \\
\hline
Q=0 & 0 & 1 & X & 0 \\
Q=1 & 1 & 1 & X & 0 \\
\hline
\end{array}
$$