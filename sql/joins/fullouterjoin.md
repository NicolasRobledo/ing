TARGET DECK
SQL desk1



# 🔗 FULL OUTER JOIN en SQL
El `FULL OUTER JOIN` devuelve:
![[fullouterjoin.png]]
- Todos los registros de la tabla **izquierda** (A)  
- Todos los registros de la tabla **derecha** (B)  
- Si no hay coincidencias, se completa con `NULL` lo que falte.
> ⚠️ *No todos los motores de bases de datos soportan `FULL OUTER JOIN` directamente (por ejemplo, MySQL no lo soporta sin emulación).*
---
## 📥 Tablas de entrada
### 🧾 Tabla: Clientes
| id_cliente | nombre |
| ---------- | ------ |
| 1          | Juan   |
| 2          | Ana    |
| 3          | Luis   |
### 🧾 Tabla: Pedidos
| id_pedido | id_cliente | producto   |
|-----------|------------|------------|
| 101       | 1          | Laptop     |
| 102       | 1          | Mouse      |
| 103       | 2          | Teclado    |
| 104       | 4          | Monitor    |
## 📤 Resultado del FULL OUTER JOIN
| id_cliente | nombre | id_pedido | producto |
|------------|--------|-----------|----------|
| 1          | Juan   | 101       | Laptop   |
| 1          | Juan   | 102       | Mouse    |
| 2          | Ana    | 103       | Teclado  |
| 3          | Luis   | NULL      | NULL     |
| 4          | NULL   | 104       | Monitor  |
 #flashcard


## 🧠 Explicación
- ✅ **Juan** tiene dos pedidos → aparece dos veces con sus productos.
- ✅ **Ana** tiene un pedido → aparece una vez.
- ❌ **Luis** no tiene pedidos → aparece con `NULL` en columnas de `Pedidos`.
- ❌ El pedido **104** está asociado a un `id_cliente = 4`, que no existe en la tabla `Clientes` → aparece con `NULL` en las columnas de `Clientes`.
## 💻 Código SQL del ejemplo
```sql
SELECT 
  Clientes.id_cliente,
  Clientes.nombre,
  Pedidos.id_pedido,
  Pedidos.producto
FROM Clientes
FULL OUTER JOIN Pedidos
  ON Clientes.id_cliente = Pedidos.id_cliente;
```
<!--ID: 1749473759082-->

