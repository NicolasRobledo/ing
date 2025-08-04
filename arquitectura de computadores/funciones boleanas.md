## Funciones Booleanas 🧮

En la generación de funciones booleanas se obtienen **tablas de verdad**.  
Es la composición de variables con sus respectivas combinaciones que determinan una tarea, y en función de eso, se obtienen diferentes resultados.

➤ Son distribuciones posibles de los valores de las variables (solo **0** y **1**), independientemente de la cantidad de variables dicotómicas (que toman 2 valores).

---

## Formas de Expresiones Booleanas

### 1. Suma de Productos (SOP) 🔌

❖ Cuando dos o más productos se suman mediante adición booleana:

$$
AB + AC
$$

❖ Reglas:

- ✅ Válido si hay complementos en una sola variable  
  Ejemplo:  
  $$
  A'B'C'
  $$

- ❌ No válido si hay complementos en varias variables  
  Ejemplo:  
  $$
  (ABC)'
  $$

❖ Implementación:

- 🔹 1 compuerta **OR**  
- 🔹 2 o más compuertas **AND**

---

### 2. Producto de Sumas (POS) 🔌

❖ Cuando dos o más términos suma se multiplican:

$$
(A + B)(A + C)
$$

❖ Reglas:

- ✅ Válido si hay complementos en una sola variable  
  Ejemplo:  
  $$
  A' + B' + C'
  $$

- ❌ No válido si hay complementos en varias variables  
  Ejemplo:  
  $$
  (A + B + C)'
  $$

❖ Implementación:

- 🔹 1 compuerta **AND**  
- 🔹 2 o más compuertas **OR**

---

## Tablas de Verdad 📋

**Definición:** Lista ordenada de entradas y salidas binarias (0 y 1).

### Pasos para construirlas:

1. **Desarrollar combinaciones**  
   ➢ Generar todas las posibles combinaciones de las variables (usando `00` a `11`).  
   ➢ Fórmula:  
   $$
   2^n = \text{combinaciones totales}
   $$  
   donde $n = \text{número de variables}$

2. **Operar con álgebra de Boole**  
   ➢ Calcular la salida para cada combinación.

---

## Ejemplos Prácticos

### Caso SOP:  
$$
ABC + AB'C
$$

- Negación = 1, No negación = 0.

- Combinaciones:

  - $ABC = 111 \Rightarrow \text{Salida} = 1$ 
  - $AB'C = 101 \Rightarrow \text{Salida} = 1$  
  - Resto de combinaciones → Salida = 0

---

### Caso POS:  
$$
(A' + B + C')(A' + B' + C)
$$

- Negación = 0, No negación = 1.

- Combinaciones:

  - $A' + B + C' = 101 \Rightarrow \text{Salida} = 0$  
  - $A' + B' + C = 110 \Rightarrow \text{Salida} = 0$

- Resultado final:  
  $$
  0 \cdot 0 = 0
  $$

---

✨ **Nota:**  
Las formas SOP y POS son esenciales para simplificar circuitos lógicos y optimizar el diseño de sistemas digitales.
