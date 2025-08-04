# Ciclo de Instrucción

El funcionamiento básico está dado por el **ciclo de instrucción**, que representa el proceso completo que la CPU realiza para ejecutar una instrucción almacenada en memoria. Se divide en **3 fases**:

## 1. Ciclo de Captación o Búsqueda (*fetch*)

- Obtiene la instrucción desde la memoria, utilizando la dirección indicada por el contador de programa (**PC**).
- Se transfiere al **MAR**, permitiendo el acceso a la instrucción, haciendo un *push* al bus de direcciones hacia la memoria.
- Luego, accede y envía la instrucción por el bus de datos hasta el **MBR** para almacenarla.
- Después, se hace un *push* hacia **IR** e **IBR**.

## 2. Ciclo de Decodificación

- Se descodifica el código de operación en el **IR** para saber si se trata de una instrucción o un dato.

## 3. Ciclo de Ejecución

- La CPU ejecuta la instrucción, que puede involucrar:
  - Operaciones aritméticas o lógicas en la **ALU**.
  - Transferencia de datos entre registros.
  - Lectura o escritura en memoria.
- Los resultados se almacenan en registros o memoria.

El programa continúa ejecutando instrucciones hasta que ocurre algún error o se apaga el equipo.

> Un programa es una lista de instrucciones que la CPU lee ordenadamente, interpreta y ejecuta una tras otra.

---

# Ciclo de Máquina

Es una unidad básica de tiempo dentro del ciclo de instrucción. Se llama **ciclo de máquina** al procedimiento que abarca todas las tareas necesarias para ejecutar completamente una instrucción almacenada en memoria.

### Etapas del Ciclo de Máquina

- **Búsqueda de una instrucción en memoria:**  
  La CPU accede a la memoria para recuperar la instrucción indicada por el **PC** y la transfiere al **IR**. El **PC** se incrementa automáticamente.

- **Lectura e interpretación de la instrucción:**  
  La instrucción en el **IR** es analizada y decodificada.

- **Ejecución de la instrucción:**  
  Se realiza la operación requerida.  
  Si no se necesita un nuevo acceso a memoria, el ciclo termina.  
  Si se necesita un operando, se realiza un nuevo acceso a memoria para completar la instrucción.

- **Almacenamiento de resultados:**  
  Los resultados generados se guardan en registros o en memoria principal.

- **Preparación para la próxima instrucción.**

> **Diferencia clave:**  
> Una instrucción puede requerir varios ciclos de máquina,  
> pero un solo **ciclo de instrucción** es como un subproceso que engloba a esos ciclos de máquina.

---

# Flujo de Direcciones (Addresses)

Son movimientos de **12 bits** entre registros:

- **Load PC:** envía los 12 bits más bajos del registro de llaves (**R.Sw.**) al **PC**.
- **Saltos (JMP, JMA, SRJ):** envía los 12 bits más bajos del **IR** al **PC**.
- **SRJ (salto a subrutina):** envía los 12 bits del **PC** al acumulador (**ACC**).
- **Búsqueda de una instrucción:** envía los 12 bits del **PC** al **MAR**.
- **Búsqueda de un operando:** envía los 12 bits más bajos del **IR** al **MAR**.
![[flujo-instruccion.png]]
---

# Flujo de Instrucciones y Operandos

Son movimientos de **16 bits** entre registros:

- **CSA:** copia los 16 bits del **R.Sw.** al **ACC**.
- **Deposit:** copia los 16 bits del **R.Sw.** al **MBR**.
- **Instrucciones:** se copian del **MBR** al **IR**.
- **LDA:** copia los 16 bits del **MBR** al **ACC**.
- **STA:** copia los 16 bits del **ACC** al **MBR**.

### Operaciones de la ALU (en el ciclo de ejecución)

- Copia los 16 bits del **ACC** al registro **Z** de la ALU.
- Copia los 16 bits del **MBR** al registro **Y** de la ALU.
- El resultado (salida de la ALU) se copia al **ACC**.
![[flujo-instrucciones-operandos.png]]