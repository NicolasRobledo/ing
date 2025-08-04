TARGET DECK
SQL desk1

# 🧠 Orden lógico de ejecución en SQL vs. Orden de escritura


## 🔄 Procesamiento lógico de la consulta (orden real de ejecución)
 #flashcard

1. **FROM**  
2. **WHERE**  
3. **GROUP BY**  
4. **HAVING**  
5. **SELECT**  
6. **ORDER BY**
<!--ID: 1749477029439-->


---

## 📄 Orden de escritura típico (como se escribe en SQL)
 #flashcard


1. **SELECT**  
2. **FROM**  
3. **WHERE**  
4. **GROUP BY**  
5. **HAVING**  
6. **ORDER BY**
<!--ID: 1749477064738-->


---

## 📊 Comparación: ¿Cómo se ve vs. Cómo se ejecuta?
 #flashcard

| Cómo se ve la consulta | Cómo se ejecuta | ¿Por qué funciona así? |
|------------------------|------------------|-------------------------|
| `SELECT`              | `FROM`           | SQL comienza con la tabla de donde toma los datos. |
| `FROM`                | `WHERE`          | SQL filtra las filas. |
| `WHERE`               | `GROUP BY`       | Verifica si hay agregaciones necesarias. |
| `GROUP BY`            | `HAVING`         | `HAVING` requiere un `GROUP BY`. |
| `HAVING`              | `SELECT`         | Después de agrupar y filtrar, selecciona las columnas. |
| `ORDER BY`            | `ORDER BY`       | Ordena los resultados finales. |
| `LIMIT`               | `LIMIT`          | Limita el número de filas devueltas. |
<!--ID: 1749477112293-->


💡 **Nota:**  
- `HAVING` se aplica después de agrupar (`GROUP BY`), a diferencia de `WHERE`, que se aplica antes.
- `SELECT` ocurre al final porque es cuando SQL ya sabe qué mostrar tras aplicar todos los filtros y agrupaciones.
