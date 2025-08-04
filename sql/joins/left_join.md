TARGET DECK
SQL desk1

# 🔗 LEFT JOIN en SQL

El `LEFT JOIN` devuelve **todos los registros de la tabla izquierda** (A) y los **coincidentes** de la tabla derecha (B).  
Si no hay coincidencia, las columnas de la tabla B se completan con `NULL`.
![[leftjoin.png]]
## 📥 Tablas de entrada
### 🧾 Tabla: Clientes
| id_cliente | nombre  |
|------------|---------|
| 1          | Juan    |
| 2          | Ana     |
| 3          | Luis    |
### 🧾 Tabla: Pedidos
| id_pedido | id_cliente | producto |
|-----------|------------|----------|
| 101       | 1          | Laptop   |
| 102       | 1          | Mouse    |
| 103       | 2          | Teclado  |
## 📤 Resultado del LEFT JOIN
| id_cliente | nombre | id_pedido | producto |
|------------|--------|-----------|----------|
| 1          | Juan   | 101       | Laptop   |
| 1          | Juan   | 102       | Mouse    |
| 2          | Ana    | 103       | Teclado  |
| 3          | Luis   | NULL      | NULL     |
 #flashcard


## 🧠 Explicación
- ✅ **Juan** tiene dos pedidos → aparece dos veces con sus productos.
- ✅ **Ana** tiene un pedido → aparece una vez.
- ❌ **Luis** no tiene pedidos → aparece con valores `NULL` en columnas de la tabla `Pedidos`.
## 💻 Código SQL del ejemplo
```sql
SELECT 
  Clientes.id_cliente,
  Clientes.nombre,
  Pedidos.id_pedido,
  Pedidos.producto
FROM Clientes
LEFT JOIN Pedidos
  ON Clientes.id_cliente = Pedidos.id_cliente;
```
<!--ID: 1749475198744-->

