TARGET DECK
SQL desk1


# 📊 Uso de `GROUP BY` en SQL
## 🧠 ¿Qué hace `GROUP BY`?
La cláusula `GROUP BY` en SQL se usa para **agrupar filas** que tienen los mismos valores en una o más columnas. Suele utilizarse junto con funciones de agregación como:
- `COUNT()`
- `SUM()`
- `AVG()`
- `MAX()`
- `MIN()`
---
## 📦 Tabla de ejemplo: `Ventas`
| id_venta | vendedor | producto | cantidad | total |
|----------|----------|----------|----------|-------|
| 1        | Ana      | Laptop   | 1        | 1000  |
| 2        | Juan     | Mouse    | 2        | 40    |
| 3        | Ana      | Teclado  | 1        | 50    |
| 4        | Juan     | Laptop   | 1        | 1000  |
| 5        | Ana      | Mouse    | 3        | 60    |
 #flashcard


## 📊 Ejemplo 1: Total de ventas por vendedor
```sql
SELECT vendedor, SUM(total) AS total_vendido
FROM Ventas
GROUP BY vendedor;
```
### Resultado:
| vendedor | total_vendido |
| -------- | ------------- |
| Ana      | 1110          |
| Juan     | 1040          |
# 📊 Ejemplo 2: Cantidad total de productos vendidos por producto
```sql
SELECT producto, SUM(cantidad) AS total_cantidad
FROM Ventas
GROUP BY producto;
```
### Resultado:
|producto|total_cantidad|
|---|---|
|Laptop|2|
|Mouse|5|
|Teclado|1|
## 🧠 Notas clave
- GROUP BY agrupa los datos basándose en los valores de una o más columnas.
- En una consulta con GROUP BY, solo se pueden mostrar:
  - Columnas que están en la cláusula GROUP BY.
  - Columnas sobre las que se aplique una función de agregación como SUM o COUNT.
✅ Es muy útil para obtener estadísticas y resúmenes agrupados a partir de grandes cantidades de datos.
<!--ID: 1749478161118-->

