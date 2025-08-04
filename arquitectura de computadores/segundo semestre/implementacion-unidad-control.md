# 🧠 Implementación de la Unidad de Control en la Máquina BLUE

La BLUE es una **máquina síncrona**, es decir, opera con un **reloj maestro** que emite pulsos en intervalos regulares (cada 125 nanosegundos). Su unidad de control se implementa con **tres biestables principales**:

## 1. RUN (Arranque)
- Tipo: Biestable **Set-Reset (S-R)**
- Función: Controla si la CPU está en ejecución.
- Se activa (`Q = 1`) con el botón `START`.
- Se desactiva (`Q = 0`) con:
  - El botón `STOP`
  - La instrucción `HALT`
  - Un **overflow aritmético**

## 2. STATE (Estado)
- Tipo: Biestable **D**
- Determina el estado de la CPU:
  - `Fetch` (búsqueda)
  - `Execute` (ejecución)

## 3. CLOCK (Reloj)
- Tipo: Biestable **Set-Reset**
- Controla el inicio y propagación de pulsos temporales (cada ciclo tiene 8 pasos de 125 ns)
- Se activa tras presionar `START` y genera una secuencia de pulsos

---

# 🔁 Ciclo de Búsqueda (Fetch Cycle)

Se activa cuando:
- `RUN` está en `ON`
- `STATE` está en modo `Fetch`

## Pulso a Pulso:
1. **Pulso 1**:  
   - El contenido del **PC** se copia a:
     - **MAR** (registro de direcciones de memoria)
     - **Registro Z** de la ALU  
   - Se inicia lectura de memoria

2. **Pulso 2**:  
   - Se coloca `+1` en el **registro Y** de la ALU

3. **Pulso 3**:  
   - Se realiza la suma `PC + 1`

4. **Pulso 4**:  
   - Se actualiza el **PC** con el resultado (PC incrementado)

5. **Pulso 5**:  
   - El dato de memoria va al **MBR** (registro buffer)

6. **Pulso 6**:  
   - El MBR se copia al **IR** (registro de instrucción)
   - Comienza la decodificación

7. **Pulso 7 y 8**:  
   - Tiempo donde la memoria no está disponible
   - Algunas instrucciones se finalizan aquí:
     - `HALT`, `NOP`, `JMP`, `JMA`, `SRJ`, `CSA`, `NOT`, `RAL`

---

# 🧪 Ejemplo de Ejecución

1. **PC = 300**  
   - Dirección con instrucción `Codop = 1`, dirección = 940  
   - Se carga dato = 3 desde memoria a AC (acumulador)

2. **PC = 301**  
   - Instrucción `Codop = 5`, dirección = 941  
   - Suma `dato(2) + AC(3) = 5`

3. **PC = 302**  
   - Instrucción `Codop = 2`, dirección = 941  
   - Guarda el contenido del AC (5) en la dirección 941

---

# 🧮 Instrucciones de Dos Ciclos

Estas requieren **dos accesos a memoria**:
- Primer ciclo: traer la instrucción
- Segundo ciclo: operar con datos de memoria

## Instrucciones que requieren ciclo de ejecución:
- `LDA` (load)
- `STA` (store)
- `ADD` (suma)
- `XOR` (operación lógica)
- `AND` (operación lógica)
- `IOR` (OR lógico)

> Estas instrucciones acceden a memoria para buscar o almacenar datos.
