TARGET DECK
SQL desk

¿Qué devuelve `UPPER('juan')`?  #flashcard
Convierte a mayúsculas → `'JUAN'`
<!--ID: 1749473756537-->




¿Qué devuelve `LOWER('LOPEZ')`?  #flashcard
Convierte a minúsculas → `'lopez'`
<!--ID: 1749473756581-->




¿Qué devuelve `LENGTH('Maria')` o `LEN('Maria')`?  #flashcard
Cuenta caracteres → `5`
<!--ID: 1749473756623-->




¿Qué devuelve `LEFT('Gonzalez', 3)`?  #flashcard
Obtiene los primeros 3 caracteres → `'Gon'`
<!--ID: 1749473756664-->




¿Qué devuelve `RIGHT('Perez', 2)`?  #flashcard
Obtiene los últimos 2 caracteres → `'ez'`
<!--ID: 1749473756706-->




¿Qué devuelve `SUBSTRING('Ramirez', 2, 4)`?  #flashcard
Extrae 4 caracteres desde la posición 2 → `'amir'`
<!--ID: 1749473756748-->




¿Qué devuelve `REVERSE('lucas')`?  #flashcard
Invierte el texto → `'sacul'`
<!--ID: 1749473756790-->




¿Qué devuelve `TRIM(' hola ')`?  #flashcard
Quita espacios a ambos lados → `'hola'`
<!--ID: 1749473756832-->




¿Qué devuelve `LTRIM(' hola')`?  #flashcard
Quita espacios a la izquierda → `'hola'`
<!--ID: 1749473756874-->




¿Qué devuelve `RTRIM('hola ')`?  #flashcard
Quita espacios a la derecha → `'hola'`
<!--ID: 1749473756915-->




¿Qué devuelve `REPLACE('telefono', 'fono', 'visión')`?  #flashcard
Reemplaza texto dentro de la palabra → `'televisión'`
<!--ID: 1749473756955-->




¿Qué devuelve `CONCAT('Ana', 'Gomez')` o `'Ana' + 'Gomez'`?  #flashcard
Une dos textos → `'AnaGomez'`
<!--ID: 1749473756988-->




¿Qué devuelve `SPACE(4)`?  #flashcard
Agrega 4 espacios → `'    '`
<!--ID: 1749473757024-->




¿Qué devuelve `ABS(-15)`?  #flashcard
Valor absoluto → `15`
<!--ID: 1749473757066-->




¿Qué devuelve `ROUND(5.78, 1)`?  #flashcard
Redondea con 1 decimal → `5.8`
<!--ID: 1749473757109-->




¿Qué devuelve `CEILING(3.2)`?  #flashcard
Redondea hacia arriba → `4`
<!--ID: 1749473757242-->




¿Qué devuelve `FLOOR(3.9)`?  #flashcard
Redondea hacia abajo → `3`
<!--ID: 1749473757285-->




¿Qué devuelve `POWER(2, 3)`?  #flashcard
Eleva a potencia → `8`
<!--ID: 1749473757326-->




¿Qué devuelve `SQRT(25)`?  #flashcard
Raíz cuadrada → `5`
<!--ID: 1749473757368-->




¿Qué devuelve `MOD(10, 3)` o `10 % 3`?  #flashcard
Resto de la división → `1`
<!--ID: 1749473757410-->




¿Qué devuelve `GETDATE()`?  #flashcard
Fecha y hora actual → `'2025-06-01 15:20:45'`
<!--ID: 1749473757453-->




¿Qué devuelve `CURRENT_TIMESTAMP`?  #flashcard
Fecha y hora actual → `'2025-06-01 15:20:45'`
<!--ID: 1749473757493-->




¿Qué devuelve `DAY('2024-04-26')`?  #flashcard
Día de la fecha → `26`
<!--ID: 1749473757535-->




¿Qué devuelve `MONTH('2024-04-26')`?  #flashcard
Mes de la fecha → `4`
<!--ID: 1749473757577-->




¿Qué devuelve `YEAR('2024-04-26')`?  #flashcard
Año de la fecha → `2024`
<!--ID: 1749473757627-->




¿Qué devuelve `DATEPART(MONTH, '2024-10-15')`?  #flashcard
Parte específica de la fecha → `10`
<!--ID: 1749473757719-->




¿Qué devuelve `DATEDIFF('2024-01-01', '2024-01-10')`?  #flashcard
Días entre fechas → `9`
<!--ID: 1749473757811-->




¿Qué devuelve `FORMAT('2024-04-26', 'dd/MM/yyyy')`?  #flashcard
Fecha formateada → `'26/04/2024'`
<!--ID: 1749473757861-->




¿Qué devuelve `COUNT(*)` en una tabla con 4 filas?  #flashcard
Cuenta filas → `4`
<!--ID: 1749473757911-->




¿Qué devuelve `SUM([10, 20, 30])`?  #flashcard
Suma valores → `60`
<!--ID: 1749473757961-->




¿Qué devuelve `AVG([5, 15, 20])`?  #flashcard
Promedio → `13.33`
<!--ID: 1749473758012-->




¿Qué devuelve `MIN([4, 8, 1, 7])`?  #flashcard
Valor mínimo → `1`
<!--ID: 1749473758054-->




¿Qué devuelve `MAX([4, 8, 1, 7])`?  #flashcard
Valor máximo → `8`
<!--ID: 1749473758096-->




¿Qué devuelve `ISNULL(NULL, 'Sin dato')`?  #flashcard
Reemplaza NULL → `'Sin dato'`
<!--ID: 1749473758137-->




¿Qué devuelve `CAST(123 AS VARCHAR)`?  #flashcard
Convierte número a texto → `'123'`
<!--ID: 1749473758179-->




¿Qué devuelve `CONVERT(VARCHAR, '2024-04-26', 103)`?  #flashcard
Convierte fecha a texto → `'26/04/2024'`
<!--ID: 1749473758221-->




¿Qué devuelve `COALESCE(NULL, NULL, 'hola')`?  #flashcard
Primer valor no nulo → `'hola'`
<!--ID: 1749473758263-->



¿Qué devuelve `CHARINDEX('a', 'Maria')`? #flashcard
Posición de la letra `'a'` → `2`
<!--ID: 1749473758304-->




¿Qué devuelve `PATINDEX('%ri%', 'Maria')`? #flashcard
Posición del patrón `'ri'` → `3`
<!--ID: 1749473758346-->




¿Qué devuelve `CASE WHEN 1 < 2 THEN 'Sí' ELSE 'No' END`? #flashcard
Evalúa condición → `'Sí'`
<!--ID: 1749473758388-->




¿Qué devuelve `RIGHT('0000' + CAST(5 AS VARCHAR), 4)`? #flashcard
Rellena con ceros a la izquierda → `'0005'`
<!--ID: 1749473758430-->




¿Qué hace `GROUP BY` en una consulta SQL? #flashcard
Agrupa filas por valores comunes para aplicar funciones agregadas
<!--ID: 1749473758471-->




¿Qué hace `HAVING` en SQL? #flashcard
Filtra resultados después del `GROUP BY`
<!--ID: 1749473758514-->




¿Qué devuelve `SELECT MAX(SALARIO) FROM empleados`? #flashcard
El salario más alto en la tabla `empleados`
<!--ID: 1749473758555-->




¿Qué hace una subconsulta escalar? #flashcard
Devuelve un único valor (un campo de una sola fila)
<!--ID: 1749473758597-->




¿Qué hace `INNER JOIN` entre dos tablas? #flashcard
Une solo las filas que tienen coincidencias en ambas tablas
<!--ID: 1749473758639-->



