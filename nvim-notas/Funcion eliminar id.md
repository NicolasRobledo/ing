---
tags: [neovim, automatización, limpieza]
---

# Script para Eliminar IDs en Neovim

## 📜 Código Principal
```lua
function _G.delete_ids()
  vim.cmd([[%g/<!--ID: \d\+-->/d]])
end
vim.keymap.set('n', '<leader>d', delete_ids, {desc = "Eliminar IDs"})
```

## 🛠️ ¿Cómo Funciona?

### 1. Patrón Regex Clave
```regex
<!--ID: \d\+-->
```
- `\d\+`: Coincide con **1 o más dígitos** numéricos (`1746289541322`, etc.)
- `<!--ID: ` y `-->`: Texto literal que enmarca el ID

### 2. Comando Global (`:g`)
```vim
:%g/<!--ID: \d\+-->/d
```
- `%`: Busca en todo el documento
- `d`: Elimina las líneas que coinciden

### 3. Mapeo de Teclas
- Se activa con `<leader>d` (modo normal)
- Descripción visible con `:WhichKey`

## 🔄 Comparación de Métodos

| Método          | Comando              | Efecto                             |
|-----------------|----------------------|------------------------------------|
| **Eliminar línea** | `:%g/<!--ID: .../d` | Borra toda la línea del ID         |
| **Reemplazar**     | `:%s/<!--ID: ...//` | Elimina solo el texto del ID       |

## 📋 Ejemplo Práctico

**Antes:**
```markdown
¿Qué ventajas ofrece...? #flashcard
- Menos costosas...
<!--ID: 1746289541368-->
```

**Después:**
```markdown
¿Qué ventajas ofrece...? #flashcard
- Menos costosas...
```
<!--ID: 1746294523326-->


## 💡 Tips Importantes
1. **Previsualización**: Verifica qué borrará con:
   ```vim
   :%g/<!--ID: \d\+-->/p
   ```
2. **Multiarchivo**: Para procesar varios archivos:
   ```vim
   :argdo g/<!--ID: \d\+-->/d
   ```
3. **Deshacer**: Recuerda que puedes revertir con `u` (undo)

> **⚠️ Precaución:** El borrado es permanente. Recomiendo `:set undofile` en Neovim para histórico de cambios ilimitado.