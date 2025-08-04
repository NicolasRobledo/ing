# Registros Serie/Paralelo (SIPO)

- Es un **híbrido** entre los registros **SISO** y **PIPO**.
    
- Utiliza **flip-flops tipo RS**, pero con una entrada **directa** y una **negada**, conformando un comportamiento equivalente a un **flip-flop tipo D**.
    

---

## Funcionamiento

- Tiene una **entrada de datos en serie**.
    
- Los datos ingresan **uno por uno** con los **flancos de subida y bajada** del reloj.
    
- Con cada **pulso de reloj**, los **bits se almacenan internamente** y se vuelcan **todos al mismo tiempo (en paralelo)** en las salidas.
    

---

## Estado Inicial

- Si se parte de un **RESET** ($\overline{\text{CLR}}$), todos los flip-flops comienzan en **0**.
    

---

## Ejemplo de funcionamiento

- Se puede usar una **entrada A** conectada a una **compuerta NOT**.
    
- Si se quiere ingresar el número binario `1101`:
    
    - Cuando **A = 1**, se activa **$S = 1$ y $R = 0$**, por lo que **$Q_0 = 1$** (se fija el dato).
        
    - Cuando **A = 0**, se activa **$S = 0$ y $R = 1$**, y **$Q_0 = 0$** (se resetea).
        
- Esto se repite para cada bit ingresado.
    

---

## Control de habilitación

- La **compuerta AND** funciona como una **palanca de habilitación**:
    
    - La entrada **A** lleva el **dato binario**.
        
    - La entrada **B**:
        
        - Si **B = 0**, **inhabilita** el circuito (no se cargan datos).
            
        - Si **B = 1**, **habilita** el paso de datos al registro.
            

---

## Señales de control

- **CLR** ($\overline{\text{CLR}}$):
    
    - Actúa de forma **asíncrona** (no depende del reloj).
        
    - Se usa exclusivamente para **resetear** el registro.
        
- **CLK** (señal de reloj):
    
    - Es de tipo **síncrono**.
        
    - Controla **cuándo se almacenan los datos**.
        
- La presencia de una **compuerta NOT** puede deberse al diseño del **fabricante**, pero **no altera el funcionamiento lógico** del circuito.

# Registros Paralelo/Serie (PISO)

- Cargan los datos de forma **paralela** y los descargan por una **única salida** en **serie**.
    
- Utilizan **flip-flops tipo D** conectados en cascada para permitir el **desplazamiento secuencial** de los bits hacia la salida.
    

---

## Modo de operación

- Disponen de una señal de control llamada **SHIFT/LOAD**:
    
    - **LOAD = 0**: Se realiza la **carga paralela** de datos en todos los flip-flops al mismo tiempo.
        
    - **SHIFT = 1**: Los datos almacenados se **desplazan** de forma secuencial hacia la salida con cada **pulso de reloj**.
        

---

## Comportamiento

- Luego de cargar los datos, el registro se comporta como un **registro de desplazamiento**.
    
- Cada pulso de reloj mueve los bits hacia la **salida serie**, empezando por el bit más significativo o el menos significativo, según el diseño.

# Registros Bidireccionales

- Son registros que permiten la **transmisión de datos en serie** hacia **ambos sentidos**:
    
    - **Hacia la derecha**
        
    - **Hacia la izquierda**
        

---

## Señal de control: `RIGHT/LEFT`

- Determina la **dirección del desplazamiento** de los datos.
RIGHT = 1 → Desplazamiento hacia la derecha  
LEFT  = 1 → Desplazamiento hacia la izquierda

- Cuando `RIGHT = 1`:
    
    - Se **inhabilitan** las compuertas AND del lado derecho.
        
- Cuando `LEFT = 0`:
    
    - Se **inhabilitan** las compuertas AND del lado izquierdo.
        

---

## Comportamiento de salida

- Dependiendo del valor de `RIGHT/LEFT`, los datos **saldrán** por:
    
    - **$Q_0$** (si se desplaza hacia la derecha)
        
    - **$Q_3$** (si se desplaza hacia la izquierda)