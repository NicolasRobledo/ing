# Funciones comunes de SQL: Resumen para repaso

## 🌣️ FUNCIONES DE TEXTO

|Función|Enunciado|Entrada|Salida|
|---|---|---|---|
|`UPPER()`|Convertir a mayúsculas|`'juan'`|`'JUAN'`|
|`LOWER()`|Convertir a minúsculas|`'LOPEZ'`|`'lopez'`|
|`LEN()` o `LENGTH()`|Calcular la cantidad de caracteres|`'Maria'`|`5`|
|`LEFT()`|Obtener los primeros 3 caracteres|`'Gonzalez'`, 3|`'Gon'`|
|`RIGHT()`|Obtener los últimos 2 caracteres|`'Perez'`, 2|`'ez'`|
|`SUBSTRING()`|Extraer 4 letras desde posición 2|`'Ramirez'`, 2, 4|`'amir'`|
|`REVERSE()`|Invertir un texto|`'lucas'`|`'sacul'`|
|`TRIM()`|Quitar espacios a ambos lados|`' hola '`|`'hola'`|
|`LTRIM()`|Quitar espacios a la izquierda|`' hola'`|`'hola'`|
|`RTRIM()`|Quitar espacios a la derecha|`'hola '`|`'hola'`|
|`REPLACE()`|Reemplazar texto dentro de una palabra|`'telefono'`, `'fono'`, `'visión'`|`'televisión'`|
|`CONCAT()` o `+`|Unir dos textos|`'Ana'`, `'Gomez'`|`'AnaGomez'`|
|`SPACE()`|Agregar 4 espacios|`SPACE(4)`|`'    '`|

---

## 📉 FUNCIONES NUMÉRICAS

|Función|Enunciado|Entrada|Salida|
|---|---|---|---|
|`ABS()`|Valor absoluto|`-15`|`15`|
|`ROUND()`|Redondear con 1 decimal|`5.78`, 1|`5.8`|
|`CEILING()`|Redondear hacia arriba|`3.2`|`4`|
|`FLOOR()`|Redondear hacia abajo|`3.9`|`3`|
|`POWER()`|Elevar a potencia|`2`, `3`|`8`|
|`SQRT()`|Raíz cuadrada|`25`|`5`|
|`MOD()` o `%`|Resto de dividir 10 entre 3|`10 % 3`|`1`|

---

## 📅 FUNCIONES DE FECHA

|Función|Enunciado|Entrada|Salida|
|---|---|---|---|
|`GETDATE()`|Obtener la fecha actual|—|`'2025-06-01 15:20:45'`|
|`CURRENT_TIMESTAMP`|Fecha y hora actual|—|`'2025-06-01 15:20:45'`|
|`DAY()`|Obtener el día de una fecha|`'2024-04-26'`|`26`|
|`MONTH()`|Obtener el mes de una fecha|`'2024-04-26'`|`4`|
|`YEAR()`|Obtener el año de una fecha|`'2024-04-26'`|`2024`|
|`DATEPART()`|Parte específica de una fecha|`MONTH, '2024-10-15'`|`10`|
|`DATEDIFF()`|Días entre dos fechas|`'2024-01-01'`, `'2024-01-10'`|`9`|
|`FORMAT()`|Mostrar fecha como texto|`'2024-04-26'`, `'dd/MM/yyyy'`|`'26/04/2024'`|

---

## 📊 FUNCIONES DE AGRUPACIÓN

| Función    | Enunciado         | Entrada           | Salida  |
| ---------- | ----------------- | ----------------- | ------- |
| `COUNT(*)` | Contar filas      | Tabla con 4 filas | `4`     |
| `SUM()`    | Sumar una columna | `[10, 20, 30]`    | `60`    |
| `AVG()`    | Promediar valores | `[5, 15, 20]`     | `13.33` |
| `MIN()`    | Mínimo valor      | `[4, 8, 1, 7]`    | `1`     |
| `MAX()`    | Máximo valor      | `[4, 8, 1, 7]`    | `8`     |

---

## 🔗 OTRAS FUNCIONES

| Función      | Enunciado                        | Entrada                               | Salida         |
| ------------ | -------------------------------- | ------------------------------------- | -------------- |
| `ISNULL()`   | Reemplazar NULL con texto        | `NULL`, `'Sin dato'`                  | `'Sin dato'`   |
| `CAST()`     | Convertir número a texto         | `CAST(123 AS VARCHAR)`                | `'123'`        |
| `CONVERT()`  | Convertir fecha a texto          | `CONVERT(VARCHAR, '2024-04-26', 103)` | `'26/04/2024'` |
| `COALESCE()` | Devolver el primer valor no nulo | `NULL, NULL, 'hola'`                  | `'hola'`       |
