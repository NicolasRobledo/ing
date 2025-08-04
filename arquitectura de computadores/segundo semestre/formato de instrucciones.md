# Formatos de Instrucción básico de la CPU

## Formato de 4 direcciones:
- **Instrucción:** `ADD A, B, C, D`
- **Descripción:** Realiza la operación $A + B$, coloca el resultado en $C$, y busca la próxima instrucción en $D$.
- **Ventajas:** No se necesita instrucción de salto incondicional. Se realiza un solo ciclo de búsqueda para los tres operandos con referencia a memoria.
- **Desventajas:** Gran longitud de palabra, lo que hace que estas máquinas no prosperaran.

## Formato de 3 direcciones:
- **Instrucción:** `ADD A, B, C`
- **Descripción:** Realiza la operación $A + B$, coloca el resultado en $C$, y busca la próxima instrucción con el uso del contador de programa (PC).
- **Ventaja:** Simplicidad en la ejecución sin necesidad de una dirección adicional para la próxima instrucción.

## Formato de 2 direcciones:
- **Instrucción:** `ADD A, B`
- **Descripción:** Realiza la operación $A + B$ y coloca el resultado en $B$. La próxima instrucción se obtiene mediante el PC.
- **Desventaja:** El operando $B$ se pierde.

## Formato de 1 dirección:
- **Instrucción:** `ADD B`
- **Descripción:** Realiza la operación $Acc + B$, coloca el resultado en el acumulador ($Acc$), y la próxima instrucción se obtiene mediante el PC.
- **Desventaja:** El primer operando ya se encuentra en el registro de la CPU ($Acc$).

## Codificación de la Instrucción:
- **Codop:** Es el código de operación (4 bits), lo que representa hasta $2^4$ operaciones diferentes.
- **Dirección:** Representa la dirección de memoria, usando 12 bits para obtener hasta $2^{12}$ direcciones posibles.

## Palabra de Instrucción y Datos:
- **Palabra de Instrucción:** Es de 32 bits (4 bytes), conteniendo un código de operación y una dirección de memoria.
- **Palabra de Datos:** Los datos a procesar, que generalmente se encuentran en memoria.

## Ejemplo de Cálculo de Direcciones:
- Si tienes **512 MB de memoria** y cada celda de memoria ocupa 4 bytes, puedes calcular la cantidad de celdas dividiendo:

$$
\frac{512 \, \text{MB}}{4 \, \text{B}} = 128 \, \text{M celdas}
$$

- Para acceder a todas las celdas de memoria, necesitas calcular la cantidad de bits de dirección. Como $128 \, \text{M} = 2^{27}$, se requieren **27 bits** para direccionar todas las celdas.

## Resumen:
- **Palabra de Instrucción:** 32 bits (4 bytes).
- **Codop:** 4 bits para representar hasta $2^4$ operaciones.
- **Dirección:** 12 bits para direccionar hasta $2^{12}$ direcciones.
