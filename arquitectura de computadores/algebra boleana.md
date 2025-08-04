# Las 12 Reglas del Álgebra de Boole  
(Con aplicaciones en compuertas lógicas)

---

## 🔹 Reglas Básicas (1–9)  
Aplican directamente a compuertas lógicas:

---

**Regla de Identidad (Suma)**  
Una entrada OR con 0 mantiene el valor original.  

$$
A + 0 = A
$$

---

**Regla de Dominancia (Suma)**  
Cualquier entrada OR con 1 resulta en 1.  

$$
A + 1 = 1
$$

---

**Regla de Identidad (Multiplicación)**  
Una entrada AND con 1 mantiene el valor original.  

$$
A \cdot 1 = A
$$

---

**Regla de Dominancia (Multiplicación)**  
Cualquier entrada AND con 0 resulta en 0.  

$$
A \cdot 0 = 0
$$

---

**Idempotencia (Suma)**  
OR de una variable consigo misma no cambia su valor.  

$$
A + A = A
$$

---

**Idempotencia (Multiplicación)**  
AND de una variable consigo misma no cambia su valor.  

$$
A \cdot A = A
$$

---

**Complemento (Suma)**  
Una variable OR con su complemento siempre es 1.  

$$
A + \overline{A} = 1
$$

---

**Complemento (Multiplicación)**  
Una variable AND con su complemento siempre es 0.  

$$
A \cdot \overline{A} = 0
$$

---

**Doble Negación**  
Equivale a la compuerta NOT en cascada.  

$$
\overline{\overline{A}} = A
$$

---

## 🔸 Reglas Derivadas (10–12)  
Se demuestran con reglas anteriores:

---

**Ley de Absorción (Suma)**  
Equivalente a simplificar un circuito OR-AND a una línea directa.  

$$
A + A \cdot B = A
$$

**Demostración:**  
$$
A + AB = A(1 + B) = A \cdot 1 = A
$$

---

**Ley de Absorción (Complemento)**  
Permite simplificar una expresión con un término y su complemento.  

$$
A + \overline{A} \cdot B = A + B
$$

**Demostración:**  
$$
A + \overline{A}B = (A + \overline{A})(A + B) = 1 \cdot (A + B) = A + B
$$

**Tabla de Verdad:**  
$$
\begin{array}{|c|c|c|c|c|}
\hline
A & B & \overline{A}B & A + \overline{A}B & A + B \\
\hline
0 & 0 & 0 & 0 & 0 \\
0 & 1 & 1 & 1 & 1 \\
1 & 0 & 0 & 1 & 1 \\
1 & 1 & 0 & 1 & 1 \\
\hline
\end{array}
$$

---

**Ley de Consenso**  
Simplifica términos redundantes en expresiones booleanas.  

$$
AB + AC + BC = AB + AC
$$

**Demostración:**  
$$
AB + AC + BC = AB + AC + BC(A + \overline{A}) = AB + AC + ABC + \overline{A}BC = AB(1 + C) + AC(1 + B) = AB + AC
$$

---

## 🧠 Teoremas de De Morgan  
Complementan las reglas del Álgebra de Boole:

---

**Primer Teorema (Equivalencia NAND)**  
Una compuerta NAND equivale a un OR con entradas negadas.  

$$
\overline{A \cdot B} = \overline{A} + \overline{B}
$$

---

**Segundo Teorema (Equivalencia NOR)**  
Una compuerta NOR equivale a un AND con entradas negadas.  

$$
\overline{A + B} = \overline{A} \cdot \overline{B}
$$

---

**Nota:**  
Las **tablas de verdad** y **demostraciones** permiten validar las equivalencias lógicas.  
Las compuertas **OR**, **AND** y **NOT** son la base para implementar estas reglas en circuitos digitales.
