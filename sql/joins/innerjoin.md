TARGET DECK
SQL desk1


# 🔗 INNER JOIN en SQL

El `INNER JOIN` devuelve **solo los registros que tienen coincidencia** entre ambas tablas (A y B) según la condición especificada.
![[innerjoin.png]]
### 🧾 Tabla: Clientes
| id_cliente | nombre  |
|------------|---------|
| 1          | Juan    |
| 2          | Ana     |
| 3          | Luis    |
### 🧾 Tabla: Pedidos
| id_pedido | id_cliente | producto   |
|-----------|------------|------------|
| 101       | 1          | Laptop     |
| 102       | 1          | Mouse      |
| 103       | 2          | Teclado    |
| 104       | 4          | Monitor    |
## 📤 Resultado del INNER JOIN
| id_cliente | nombre | id_pedido | producto |
|------------|--------|-----------|----------|
| 1          | Juan   | 101       | Laptop   |
| 1          | Juan   | 102       | Mouse    |
| 2          | Ana    | 103       | Teclado  |
 #flashcard

## 🧠 Explicación
- ✅ **Juan** tiene dos pedidos → aparece dos veces con sus productos.
- ✅ **Ana** tiene un pedido → aparece una vez.
- ❌ **Luis** no tiene pedidos → no aparece.
- ❌ El pedido **104** no tiene un cliente en la tabla `Clientes` → no aparece.
## 💻 Código SQL del ejemplo
```sql
SELECT 
  Clientes.id_cliente,
  Clientes.nombre,
  Pedidos.id_pedido,
  Pedidos.producto
FROM Clientes
INNER JOIN Pedidos
  ON Clientes.id_cliente = Pedidos.id_cliente;
```
<!--ID: 1749475149628-->



