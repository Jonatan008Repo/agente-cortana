# Agente Cortana

Repositorio para llevar el control de cambios y actualizaciones del agente personalizado **Cortana**.

## Descripción

Cortana es un agente personalizado diseñado para asistir y automatizar tareas. Este repositorio centraliza el seguimiento de su desarrollo, versiones y mejoras a lo largo del tiempo.

## Estructura del Proyecto

```
agente-cortana/
├── README.md           # Documentación principal del proyecto
├── CHANGELOG.md        # Historial de cambios y versiones
├── src/                # Código fuente del agente
│   └── cortana.py      # Módulo principal del agente
└── docs/               # Documentación adicional
    └── configuracion.md
```

## Comenzar

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Jonatan008Repo/agente-cortana.git
   cd agente-cortana
   ```

2. Revisar el historial de cambios en [CHANGELOG.md](CHANGELOG.md).

## Control de Cambios

Todos los cambios, mejoras y correcciones se documentan en el archivo [CHANGELOG.md](CHANGELOG.md) siguiendo el formato [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).

Las versiones siguen el estándar [Versionado Semántico](https://semver.org/lang/es/):
- **MAJOR**: cambios incompatibles con versiones anteriores
- **MINOR**: nuevas funcionalidades compatibles con versiones anteriores
- **PATCH**: correcciones de errores compatibles con versiones anteriores

## Contribuir

1. Crear una rama para el cambio: `git checkout -b feature/mi-nueva-funcionalidad`
2. Realizar los cambios y documentarlos en `CHANGELOG.md` bajo la sección `[Sin publicar]`
3. Hacer commit con un mensaje descriptivo
4. Abrir un Pull Request

## Licencia

Este proyecto es de uso personal y privado.
