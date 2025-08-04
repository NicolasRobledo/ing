TARGET DECK
SQL desk1

# 🧾 Ejemplo de Inserción de Datos en una Tabla SQL
## 📋 Tabla: Clientes
| id_cliente | nombre | ciudad        |
|------------|--------|---------------|
| *(vacío)*  | *(vacío)* | *(vacío)*   |
Queremos insertar tres registros en la tabla `Clientes`.
```sql
INSERT INTO Clientes (id_cliente, nombre, ciudad)
VALUES
  (1, 'Juan', 'Buenos Aires'),
  (2, 'Ana', 'Córdoba'),
  (3, 'Luis', 'Rosario');
```
  #flashcard


## 🧪 Datos a insertar
- **Cliente 1**: Juan, de Buenos Aires
- **Cliente 2**: Ana, de Córdoba
- **Cliente 3**: Luis, de Rosario
## ✅ Resultado esperado en la tabla
| id_cliente | nombre | ciudad        |
|------------|--------|---------------|
| 1          | Juan   | Buenos Aires  |
| 2          | Ana    | Córdoba       |
| 3          | Luis   | Rosario       |
<!--ID: 1749478524931-->


> Esta tabla ahora tiene tres registros nuevos gracias al uso del comando `INSERT INTO`.
