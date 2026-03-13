# Configuración del Agente Cortana

## Parámetros Principales

| Parámetro | Descripción | Valor por defecto |
|-----------|-------------|-------------------|
| `nombre`  | Nombre del agente | `"Cortana"` |
| `version` | Versión del agente | `"0.1.0"` |

## Personalización

Para personalizar el agente, modificar los parámetros en `src/cortana.py`:

```python
agente = Cortana(nombre="MiCortana")
```

## Actualizaciones

Al actualizar el agente:

1. Modificar el código fuente en `src/`
2. Actualizar el número de versión en `src/cortana.py`
3. Documentar los cambios en `CHANGELOG.md`
4. Crear un tag con la nueva versión:
   ```bash
   git tag -a v1.0.0 -m "Versión 1.0.0"
   git push origin v1.0.0
   ```
