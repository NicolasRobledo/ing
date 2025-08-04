TARGET DECK
SQL desk1

# 🔢 ¿Qué es la cardinalidad?

La **cardinalidad** es la relación que existe entre los registros de una tabla con otra. Puede ser de varios tipos: #flashcard

- 🧍‍♂️ Uno a uno (1:1)
- 🧍‍♂️➡️🧑‍🤝‍🧑 Uno a muchos (1:N)
- 🧑‍🤝‍🧑↔️🧑‍🤝‍🧑 Muchos a muchos (N:M)
<!--ID: 1749477197389-->


---

## 🧱 Ejemplo 1: Uno a muchos (1:N)
### 🧾 Tabla: Clientes
| id_cliente | nombre |
|------------|--------|
| 1          | Juan   |
| 2          | Ana    |
### 🧾 Tabla: Pedidos
| id_pedido | id_cliente | producto |
|-----------|------------|----------|
| 101       | 1          | Laptop   |
| 102       | 1          | Mouse    |
| 103       | 2          | Teclado  |
 #flashcard


✅ **Relación:**
- Un cliente puede tener **muchos pedidos**.
- Cada pedido pertenece a **un solo cliente**.
📌 **Cardinalidad:** 1 cliente : N pedidos  
🧭 Esto es una relación **de uno a muchos (1:N)**.
<!--ID: 1749477782828-->


---

## 🧱 Ejemplo 2: Muchos a muchos (N:M)
### 🧾 Tabla: Estudiantes
| id_estudiante | nombre  |
|---------------|---------|
| 1             | María   |
| 2             | Pablo   |
### 🧾 Tabla: Cursos
| id_curso | curso     |
|----------|-----------|
| 1        | Matemática |
| 2        | Historia   |
### 🧾 Tabla intermedia: Estudiantes_Cursos
| id_estudiante | id_curso |
|---------------|----------|
| 1             | 1        |
| 1             | 2        |
| 2             | 1        |
 #flashcard


✅ **Relación:**
- Un estudiante puede inscribirse en **varios cursos**.
- Un curso puede tener **muchos estudiantes**.
📌 **Cardinalidad:** N estudiantes : M cursos  
🧭 Esto es una relación **de muchos a muchos (N:M)**.
<!--ID: 1749477782901-->



---

## 🧱 Ejemplo 3: Uno a uno (1:1)
### 🧾 Tabla: Personas
| id_persona | nombre |
|------------|--------|
| 1          | Laura  |
| 2          | Pedro  |
### 🧾 Tabla: Pasaportes
| id_pasaporte | id_persona | número  |
|--------------|------------|---------|
| 1001         | 1          | AB12345 |
| 1002         | 2          | XY67890 |
 #flashcard


✅ **Relación:**
- Cada persona tiene **un solo pasaporte**.
- Cada pasaporte pertenece a **una sola persona**.
📌 **Cardinalidad:** 1 persona : 1 pasaporte  
🧭 Esto es una relación **de uno a uno (1:1)**.
<!--ID: 1749477782959-->


---

## 📊 ¿Cómo identificar la cardinalidad?
 #flashcard

| Regla | Tipo de relación |
|-------|------------------|
| Una tabla tiene una FK hacia otra tabla con PK | 1:N |
| Hay una tabla intermedia con dos FKs hacia otras tablas | N:M |
| Una PK es también FK sin repetirse | 1:1 |
<!--ID: 1749477783009-->


---

## 🧱 Representación estilo hoja de cálculo (Excel)

| Entidad  | Atributos                                       |
|----------|--------------------------------------------------|
| Cliente  | id_cliente (PK), nombre                          |
| Pedido   | id_pedido (PK), id_cliente (FK), producto        |

✅ `id_cliente` es clave primaria en Cliente y clave foránea en Pedido → **Relación 1:N**

---

> ¿Querés que te ayude con un ejemplo real que te hayan dado? Pasame las dos tablas y te digo qué cardinalidad tienen.
