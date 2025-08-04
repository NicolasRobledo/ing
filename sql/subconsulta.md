TARGET DECK
SQL desk1

# 🔗 Subconsulta en SQL
Una **subconsulta** es una consulta anidada dentro de otra consulta SQL.  
Se usa para obtener un conjunto de resultados que luego se utiliza en la consulta principal, permitiendo hacer consultas más complejas y dinámicas.
---
## 📥 Tablas de entrada
### 🧾 Tabla: Empleados
| id_empleado | nombre | departamento_id |
| ----------- | ------ | --------------- |
| 1           | María  | 10              |
| 2           | Pedro  | 20              |
| 3           | Laura  | 10              |
### 🧾 Tabla: Departamentos
| departamento_id | nombre_depto |
| --------------- | ------------ |
| 10              | Ventas       |
| 20              | Marketing    |
## 📤 Resultado de la consulta con subconsulta
Queremos obtener los empleados que trabajan en el departamento de Ventas. Primero, buscamos el `departamento_id` del departamento "Ventas" con una subconsulta, y luego filtramos los empleados.
### tabla Salida:
| id_empleado | nombre | departamento_id |
| ----------- | ------ | --------------- |
| 1           | María  | 10              |
| 3           | Laura  | 10              |
 #flashcard


## 🧠 Explicación
- ✅ La subconsulta `(SELECT departamento_id FROM Departamentos WHERE nombre_depto = 'Ventas')` obtiene el id del departamento Ventas (10).
- ✅ La consulta principal selecciona los empleados cuyo `departamento_id` coincide con ese resultado.
- Esto permite filtrar empleados sin tener que saber el `departamento_id` exacto a mano.
## 💻 Código SQL del ejemplo
```sql
SELECT 
  id_empleado, 
  nombre, 
  departamento_id
FROM Empleados
WHERE departamento_id = (
  SELECT departamento_id
  FROM Departamentos
  WHERE nombre_depto = 'Ventas'
);
```
<!--ID: 1749475683712-->


