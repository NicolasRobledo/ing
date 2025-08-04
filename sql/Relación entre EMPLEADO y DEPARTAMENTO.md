**Relación entre EMPLEADO y DEPARTAMENTO**
![[empleados.png]]

- Un DEPARTAMENTO puede tener muchos EMPLEADOS (1:N).
- Un EMPLEADO pertenece a un solo DEPARTAMENTO.

**EMPLEADO**
- ID (PK)
- Dept_ID (FK → DEPARTAMENTO.ID)
- Nombre
- Apellido
- Salario

**DEPARTAMENTO**
- ID (PK)
- Nombre
- Ubicación
- Color
