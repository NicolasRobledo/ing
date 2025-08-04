TARGET DECK
SQL desk1

# 🔁 RIGHT JOIN en SQL
El `RIGHT JOIN` devuelve **todos los registros de la tabla derecha** (B) y los **coincidentes** de la tabla izquierda (A).  
Si no hay coincidencia, las columnas de la tabla A se completan con `NULL`.
![[rightjoin.png]]
## 📥 Tablas de entrada
### 🧾 Tabla: Clientes
| id_cliente | nombre |
| ---------- | ------ |
| 1          | Juan   |
| 2          | Ana    |
| 3          | Luis   |
### 🧾 Tabla: Pedidos
|id_pedido|id_cliente|producto|
|---|---|---|
|101|1|Laptop|
|102|1|Mouse|
|103|2|Teclado|
|104|4|Monitor|
## 📤 Resultado del RIGHT JOIN
| id_cliente | nombre | id_pedido | producto |
|------------|--------|-----------|----------|
| 1          | Juan   | 101       | Laptop   |
| 1          | Juan   | 102       | Mouse    |
| 2          | Ana    | 103       | Teclado  |
| NULL       | NULL   | 104       | Monitor  |
 #flashcard


## 📌 Explicación
- ✅ Juan tiene dos pedidos.
- ✅ Ana tiene uno.
- ❌ El pedido 104 está asociado a un cliente inexistente (id_cliente = 4), así que las columnas de la tabla `Clientes` aparecen como `NULL`.
## 💻 Código SQL del ejemplo
```sql
SELECT 
  Clientes.id_cliente,
  Clientes.nombre,
  Pedidos.id_pedido,
  Pedidos.producto
FROM Clientes
RIGHT JOIN Pedidos
  ON Clientes.id_cliente = Pedidos.id_cliente;
```
<!--ID: 1749475357946-->

