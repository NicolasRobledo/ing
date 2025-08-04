Quiero que generes tarjetas tipo Cloze para usar en Obsidian con el plugin de sincronización con Anki. Estas tarjetas deben seguir estrictamente el siguiente formato:

1. **Estructura general obligatoria**:
   - La tarjeta comienza con la palabra **START** (sin espacio al final).
   - Luego va la palabra **Hueco** (sin espacio).
   - Después la palabra **Texto** (sin espacio).
   - Luego el contenido formateado en Markdown con tarjetas Cloze (`{{c1::...}}`, `{{c2::...}}`, etc.).
   - Finaliza con:
     - La línea `Tags:obsidian_cloze` (todo sin espacio extra).
     - Una línea con un comentario HTML con ID, por ejemplo: `<!--ID:1749667185427-->`
     - La palabra **END** sola en una línea (sin espacio).

2. **Sobre las tarjetas Cloze**:
   - Cada bloque de contenido debe estar agrupado en una sola cloze si es una idea completa.
   - Usar lo minimos huecos por tarjeta para no saturar.
   - Los huecos deben ir con sintaxis `{{c1:: ... }}`, `{{c2:: ... }}`, etc., sin anidar ni usar en los títulos.
   - Los títulos no deben tener Cloze.

3. **Estilo del contenido**:
   - Markdown válido para Obsidian (subtítulos, listas, negritas).
   - Si se incluye una imagen, usar el formato `![[nombre de la imagen.png]]` dentro del bloque adecuado.
   - Todo debe estar pensado para ser compatible con revisión en Anki desde Obsidian.

4. **Ejemplo exacto del formato que quiero**:

````markdown
START
Hueco
Texto
### 1. Definición de liderazgo

{{c1::El liderazgo es la capacidad de influir en un grupo para lograr una meta.}}

{{c2::Existen varios estilos de liderazgo: autocrático, democrático y liberal.}}

{{c3::Un buen líder combina autoridad con empatía y visión estratégica.}}

Tags:obsidian_cloze
<!--ID:1749667185427-->
<!--ID: 1749669248296-->
END
