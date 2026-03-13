"""
Agente Cortana - Módulo Principal

Agente personalizado para asistencia y automatización de tareas.
"""

__version__ = "0.1.0"


class Cortana:
    """Agente personalizado Cortana."""

    def __init__(self, nombre: str = "Cortana"):
        self.nombre = nombre
        self.version = __version__

    def saludar(self) -> str:
        """Retorna un saludo del agente."""
        return f"Hola, soy {self.nombre} versión {self.version}. ¿En qué puedo ayudarte?"

    def obtener_version(self) -> str:
        """Retorna la versión actual del agente."""
        return self.version


if __name__ == "__main__":
    agente = Cortana()
    print(agente.saludar())
