# Circuitos Combinacionales y Secuenciales

## Decodificadores
### Definición
- **Circuito combinacional** con $n$ entradas y $m = 2^n$ salidas.
- Cada salida representa un **minitérmino** de las entradas.
- **Tabla típica**: Matriz con `0`s y una diagonal de `1`s.

### Decodificador 2x4
$$
\begin{array}{|c|c|c|c|c|c|}
\hline
\mathbf{X} & \mathbf{Y} & \mathbf{D_0} & \mathbf{D_1} & \mathbf{D_2} & \mathbf{D_3} \\
\hline
0 & 0 & 1 & 0 & 0 & 0 \\
0 & 1 & 0 & 1 & 0 & 0 \\
1 & 0 & 0 & 0 & 1 & 0 \\
1 & 1 & 0 & 0 & 0 & 1 \\
\hline
\end{array}
$$

**Aplicación en funciones booleanas**:  
Unir salidas activas (`1`) con compuertas **OR** (o **NAND** para lógica negada).

---

## Demultiplexores
### Características
- **Decodificador + Enable ($E$)** → Controla la activación del circuito.
- **Ejemplo 1x4**:  
  - 1 entrada de datos  
  - 2 líneas de selección  
  - 4 salidas  

### Tabla de Verdad (Demux 1x4)
$$
\begin{array}{|c|c|c|c|c|c|}
\hline
\mathbf{E} & \mathbf{A} & \mathbf{B} & \mathbf{D_0} & \mathbf{D_1} & \mathbf{D_2} & \mathbf{D_3} \\
\hline
1 & X & X & 1 & 1 & 1 & 1 \\
0 & 0 & 0 & 0 & 1 & 1 & 1 \\
0 & 0 & 1 & 1 & 0 & 1 & 1 \\
0 & 1 & 0 & 1 & 1 & 0 & 1 \\
0 & 1 & 1 & 1 & 1 & 1 & 0 \\
\hline
\end{array}
$$

---

## Codificadores
### Definición
- **Función inversa a decodificadores**: $2^n$ entradas → $n$ salidas.
- **Prioridad**: Si múltiples entradas están activas, codifica la de mayor peso.

### Ejemplo (8x3 con prioridad)
$$
\begin{array}{|c|c|c|c|c|c|c|c|c|c|}
\hline
\mathbf{D_7} & \mathbf{D_6} & \mathbf{D_5} & \mathbf{D_4} & \mathbf{D_3} & \mathbf{D_2} & \mathbf{D_1} & \mathbf{D_0} & \mathbf{Z} & \mathbf{Y} & \mathbf{X} \\
\hline
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & X & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0 & 1 & X & X & 0 & 1 & 0 \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
1 & X & X & X & X & X & X & X & 1 & 1 & 1 \\
\hline
\end{array}
$$

---

## Multiplexores (MUX)
### Funcionamiento
- Selecciona 1 de $2^n$ entradas usando $n$ líneas de control.
- **Ejemplo MUX 4x1**:
$$
\begin{array}{|c|c|c|c|}
\hline
\mathbf{S_1} & \mathbf{S_0} & \text{Salida} \\
\hline
0 & 0 & I_0 \\
0 & 1 & I_1 \\
1 & 0 & I_2 \\
1 & 1 & I_3 \\
\hline
\end{array}
$$

### Tabla de Verdad (MUX 8x1)
$$
\begin{array}{|c|c|c|c|c|c|c|c|c|c|}
\hline
\mathbf{E} & \mathbf{A} & \mathbf{B} & \mathbf{C} & \mathbf{D_0} & \mathbf{D_1} & \mathbf{D_2} & \mathbf{D_3} & \mathbf{D_4} & \mathbf{D_5} & \mathbf{D_6} & \mathbf{D_7} \\
\hline
1 & X & X & X & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
0 & 0 & 0 & 1 & 1 & 0 & 1 & 1 & 1 & 1 & 1 & 1 \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
\hline
\end{array}
$$

---

