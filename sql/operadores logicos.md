## Operadores de Comparación

Estos operadores comparan valores y se usan en condiciones para filtrar datos.

| Operador              | Significado               | Ejemplo                    | Descripción                                              |
| --------------------- | ------------------------- | -------------------------- | -------------------------------------------------------- |
| `=`                   | Igual a                   | `edad = 30`                | Selecciona filas donde edad es igual a 30                |
| `!=` o `<>`           | Diferente de              | `salario <> 4000`          | Selecciona filas donde salario es distinto a 4000        |
| `<`                   | Menor que                 | `edad < 25`                | Selecciona filas donde edad es menor a 25                |
| `>`                   | Mayor que                 | `salario > 3000`           | Selecciona filas donde salario es mayor a 3000           |
| `<=`                  | Menor o igual que         | `edad <= 30`               | Selecciona filas donde edad es menor o igual a 30        |
| `>=`                  | Mayor o igual que         | `salario >= 2800`          | Selecciona filas donde salario es mayor o igual a 2800   |
| `BETWEEN ... AND ...` | Entre un rango            | `edad BETWEEN 20 AND 30`   | Selecciona filas donde edad está entre 20 y 30 inclusive |
| `IN`                  | En un conjunto de valores | `nombre IN ('Ana','Juan')` | Selecciona filas donde nombre sea Ana o Juan             |
| `LIKE`                | Coincide con patrón       | `nombre LIKE 'J%'`         | Selecciona filas donde nombre empiece con J              |

## Operadores Lógicos

Se usan para combinar o modificar condiciones.

|Operador|Significado|Ejemplo|Descripción|
|---|---|---|---|
|`AND`|Y lógico (todas true)|`edad > 25 AND salario > 3000`|Selecciona filas que cumplen ambas condiciones|
|`OR`|O lógico (alguna true)|`edad < 25 OR salario > 4000`|Selecciona filas que cumplen alguna de las condiciones|
|`NOT`|Negación|`NOT edad = 30`|Selecciona filas que **no** cumplen la condición|
## Ejemplo completo
```sql
SELECT * FROM empleados
WHERE (edad >= 25 AND salario < 5000) OR nombre = 'María';

```
Trae empleados que tengan edad mayor o igual a 25 **y** salario menor a 5000, **o** que se llamen María.
## Resumen

- **Comparación:** Permiten evaluar condiciones entre columnas y valores.
- **Lógicos:** Permiten combinar varias condiciones para filtrar resultados de forma más precisa.
- Usar paréntesis para agrupar condiciones y controlar el orden de evaluación.