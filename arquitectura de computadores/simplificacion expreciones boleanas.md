## Simplificación de Funciones Booleanas 🛠️

**Objetivo:** Reducir expresiones booleanas para minimizar el uso de puertas lógicas en circuitos digitales.

### Métodos principales:

- **Álgebra de Boole** 🧠  
- **Mapas de Karnaugh (K-Map)** 🗺️

---

## Formas Canónicas

### 1. Minterminos (Suma de Productos - SOP) 🔌

**Definición:** Suma de productos donde la salida en la tabla de verdad es 1.  
**Regla:** Se niegan las variables con valor 0.

**Ejemplo:**

Si la tabla de verdad tiene dos unos:

Expresión:  
$$
AB' + AB
$$

Simplificación:  
$$
AB' + AB = A(B' + B) = A \cdot 1 = A \quad \text{✅}
$$

---

### 2. Maxitérminos (Producto de Sumas - POS) 🔌

**Definición:** Producto de sumas donde la salida en la tabla de verdad es 0.  
**Regla:** Se niegan las variables con valor 1.

**Ejemplo:**

Si la tabla de verdad tiene dos ceros:

Expresión:  
$$
(A + B)(A + B')
$$

Simplificación:  
$$
(A + B)(A + B') = A + (B \cdot B') = A + 0 = A \quad \text{✅}
$$

---

## Regla de Elección 🚦

- Usa **minitérminos** si hay menos unos en la salida.  
- Usa **maxitérminos** si hay menos ceros.

---

## Mapas de Karnaugh (K-Map) 🗺️

**Definición:** Matriz que representa combinaciones de variables para simplificar expresiones booleanas.

### Características:

- **Número de celdas:**  
  $$
  2^n \quad \text{(donde } n = \text{número de variables)}
  $$

- **Organización:**

  - Filas: Valores de variables principales (ej: $A$)  
  - Columnas: Valores de variables secundarias (ej: $B, C$)

- **Ejemplo para 3 variables:**

  Secuencia de columnas (Gray code):  
  `00 → 01 → 11 → 10` (solo cambia un bit a la vez)

---
