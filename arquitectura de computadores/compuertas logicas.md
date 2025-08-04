# ¿Por qué se emplea el sistema binario en los sistemas digitales?

TARGET DECK
Arquitectura_de_los_computadores

¿Por qué se emplea el sistema binario en los sistemas digitales? #flashcard
El sistema binario se utiliza en los sistemas digitales porque tiene **dos posibles valores**: `1` y `0` (estado de encendido y apagado). 
<!--ID: 1746289541322-->





¿Qué ventajas ofrece el sistema binario en los sistemas digitales? #flashcard
- **Fáciles de diferenciar**, lo que **reduce la probabilidad de error en la interpretación**.
- **Menos costosas y menos complejas** de implementar.
- **Más resistentes a factores externos** como la temperatura, el envejecimiento y el ruido.
<!--ID: 1746289541368-->





¿Cómo se llama un dígito binario individual? #flashcard 
**bit**.
<!--ID: 1746289541409-->




¿Qué se puede representar agrupando varios bits? #flashcard 
Se pueden representar otros **símbolos discretos** como:
- Números decimales  
- Letras del alfabeto
<!--ID: 1746289541451-->




¿Qué permiten crear los bits en los sistemas digitales además de representar números y letras? #flashcard 
Permiten desarrollar conjuntos completos de instrucciones para el funcionamiento de los sistemas digitales.
<!--ID: 1746289541493-->






**AND** Multiplicación lógica
![[and.jpg]] #flashcard
$$
\begin{array}{|c|c|c|}
\hline
A & B & A \land B \\
\hline
0 & 0 & 0 \\
0 & 1 & 0 \\
1 & 0 & 0 \\
1 & 1 & 1 \\
\hline
\end{array}
$$
<!--ID: 1746289541536-->






**OR** – Suma lógica
![[or.jpg]] #flashcard 
$$\begin{array}{|c|c|c|}
\hline
A & B & A \lor B \\
\hline
0 & 0 & 0 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
1 & 1 & 1 \\
\hline
\end{array}
$$
<!--ID: 1746289541602-->





**NAND** – Negación de AND
![[nand.jpg]]
**OR**-Negativa

![[or-negativa.png]] #flashcard
$$
\begin{array}{|c|c|c|}
\hline
A & B & \lnot (A \land B) \\
\hline
0 & 0 & 1 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
1 & 1 & 0 \\
\hline
\end{array}
$$
<!--ID: 1746289541644-->







**NOT** – Negación lógica
![[not.jpg]] #flashcard 
$$
\begin{array}{|c|c|}
\hline
A & \lnot A \\
\hline
0 & 1 \\
1 & 0 \\
\hline
\end{array}
$$
<!--ID: 1746289541686-->



**NOR** – Negación de OR  ![[nor.jpg]]
![[and-negativa.png]] #flashcard
$$
\begin{array}{|c|c|c|}
\hline
A & B & \lnot (A \lor B) \\
\hline
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0 \\
1 & 1 & 0 \\
\hline
\end{array}
$$
<!--ID: 1746289541728-->




**XOR** – OR exclusivo  ![[xor.jpg]] #flashcard
$$
\begin{array}{|c|c|c|}
\hline
A & B & A \oplus B \\
\hline
0 & 0 & 0 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
1 & 1 & 0 \\
\hline
\end{array}
$$
<!--ID: 1746289630082-->

**XNOR** – Negación de XOR ![[xnor.jpg]] #flashcard
$$
\begin{array}{|c|c|c|}
\hline
A & B & \lnot (A \oplus B) \\
\hline
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0 \\
1 & 1 & 1 \\
\hline
\end{array}
$$
<!--ID: 1746290014828-->







END
