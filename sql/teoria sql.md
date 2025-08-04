# SELECT en Bases de Datos

## ¿Qué es SELECT?

La sentencia `SELECT` es una instrucción del lenguaje SQL utilizada para **consultar o extraer datos** de una o más tablas dentro de una base de datos relacional.

## Sintaxis básica

SELECT columna1, columna2, ...  
FROM nombre_de_tabla;

## Ejemplos

### Ejemplo 1: Seleccionar todas las columnas

SELECT * FROM usuarios  
Este comando devuelve **todos los datos** de la tabla `usuarios`.

### Ejemplo 2: Seleccionar columnas específicas

SELECT nombre, edad FROM usuarios  
Este comando devuelve solo las columnas `nombre` y `edad`.

### Ejemplo 3: Usar condiciones con WHERE

SELECT nombre FROM usuarios WHERE edad > 25  
Este comando devuelve los nombres de los usuarios cuya edad es mayor a 25.

## Notas adicionales

- `*` significa **todas las columnas**.  
- `WHERE` se utiliza para **filtrar registros** según una condición.  
- Puedes combinar `SELECT` con otras cláusulas como `ORDER BY`, `LIMIT`, `JOIN`, entre otras.
