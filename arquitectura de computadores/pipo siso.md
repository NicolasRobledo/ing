# Registros Paralelo-Paralelo (PIPO)

- Es un grupo de **flip-flops (FFs) tipo D** que puede almacenar varios bits al mismo tiempo.
    
- Los datos están disponibles de manera directa y se utiliza para la **transferencia sincrónica** de datos **en paralelo** (todos al mismo tiempo).
    

---

## Almacenamiento

- Para almacenar **8 bits**, se necesitan **8 flip-flops tipo D**, disparados por **flancos de bajada** (lo que está rodeado de rojo).
    
- Por eso se coloca una **compuerta NOT** en la entrada del reloj, para que actúe con los **flancos de subida**.
    

---

## Funcionamiento

- Todos los FFs están **sincronizados por una misma señal de reloj** ($\text{CLK}$).
    
- Las entradas pueden estar **desfasadas**, pero los datos se extraen de forma **sincrónica** (todo a la vez) con el **flanco de bajada**.
    

---

## Señal de Clear

- La señal $\overline{\text{CLR}}$ **resetea** los 8 biestables al mismo tiempo.
    
- Cuando $\overline{\text{CLR}} = 1$, los flip-flops funcionan normalmente.
    
- Cuando $\overline{\text{CLR}} = 0$, todos se reinician (nivel bajo).
    

---

## Comportamiento del reloj

- Si hay un **flanco de subida** en el reloj:
    
    - Si el dato de entrada es **alto**, se almacena el valor alto.
        
    - Si el dato es **bajo**, se almacena un nivel bajo.
        
- Si hay un **flanco de bajada**, se **mantiene** el dato previamente almacenado.
    

---

## Símbolo ANSI

- Muestra un **módulo común de control**, con:
    
    - Una señal de **EN** (Enable).
        
    - Una señal de **reloj** ($\text{CLK}$).
        
- El símbolo puede estar invertido respecto al funcionamiento real (verificar lógica).


# Registros Serie-Serie (SISO)

- Un **registro de desplazamiento** del tipo **entrada en serie / salida en serie** (SISO) **carga los datos un bit a la vez**.
    
- Utiliza **flip-flops tipo D** conectados en **cascada**.
    

---

## Funcionamiento

- Los datos se **desplazan bit por bit** con cada **pulso de reloj**, ya sea en el **flanco de subida** ($\uparrow$) o de **bajada** ($\downarrow$).
    
- Cada pulso de reloj mueve el bit almacenado al **siguiente flip-flop**.
    
- El dato avanza desde la entrada hasta el extremo opuesto del registro.
    

---

## Salida

- Con **pulsos de reloj continuos**, los bits cargados **salen uno por uno** en el **mismo orden en el que ingresaron**.
    
- Es ideal para **transmisión secuencial** de datos o como **retardo digital**.
$$
\begin{array}{c}
\text{Pulso de reloj: } \uparrow \downarrow \uparrow \downarrow \dots \\
\text{Estado del registro cambia con cada flanco:} \\
\text{[D1]} \rightarrow \text{[D2]} \rightarrow \text{[D3]} \rightarrow \text{[D4]} \rightarrow \text{[D5]} \\
\Downarrow \\
\text{Salida bit a bit en orden de entrada}
\end{array}
$$
En una imagen típica, se indica cómo **cambia el estado del registro** con cada pulso de reloj, destacando:

- **Cuándo entra el dato**.
    
- **Cómo se propaga**.
    
- **Cuándo sale por la salida**.
