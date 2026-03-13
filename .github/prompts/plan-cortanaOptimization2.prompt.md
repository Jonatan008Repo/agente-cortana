## Plan: Optimización Balanceada de Cortana

Optimizar el agente para que responda más rápido en consultas simples, mantenga alta precisión técnica en tareas complejas y amplíe cobertura de stack, sin romper su estilo actual ni sus reglas clave.

**Pasos**
1. Fase 1: Baseline y métricas
Definir criterios de éxito antes de cambios: rapidez percibida en consultas simples, precisión de propuestas, claridad de flujo y cumplimiento de autorización previa.

2. Fase 2: Flujo SDD condicional (núcleo)
Cambiar de “siempre 6 secciones” a 3 modos:
- Modo rápido para dudas puntuales y debugging corto.
- Modo completo para features y cambios grandes.
- Modo revisión para optimización/refactor acotado.
Dependencia: bloquea fases 3 a 6.

3. Fase 3: Reglas de decisión y datos críticos
Definir qué preguntar según tipo de solicitud para evitar fricción y ambigüedad. Aclarar cuándo preguntar y cuándo proponer siguiente paso directo.

4. Fase 4: Expansión de stack con fallback
Ampliar tecnologías preferidas y añadir regla explícita para stacks no listados, manteniendo compatibilidad con lo ya definido.

5. Fase 5: Ajuste de tono y ejemplos
Conservar personalidad y ejemplos de Cortana, reforzando que cada respuesta siga esta estructura: Observación rápida de la situación, análisis lógico o dato técnico, comentario irónico o humano, e instrucción clara.

6. Fase 6: Simplificación del soporte de commits
Reducir fricción de interacción inicial sin perder controles esenciales: ticket, prefijo y confirmación final.

7. Fase 7: Documentación de uso
Completar onboarding en README con quick start, explicación de modos y ejemplos de invocación.

8. Fase 8: Verificación funcional por escenarios
Probar batería de prompts por modo para validar que el flujo condicional funciona y que las reglas operativas se mantienen.

**Archivos relevantes**
- src/Cortana.agent.md: flujo SDD, identidad, stack, reglas operativas y commits.
- README.md: documentación de entrada y guía de uso.

**Verificación**
1. Probar 5 consultas simples: deben usar modo rápido sin plantilla extensa.
2. Probar 3 solicitudes de feature: deben activar modo completo con estructura SDD completa.
3. Probar 3 solicitudes de revisión/refactor: deben activar modo revisión.
4. Probar 2 solicitudes con stack fuera de lista: debe activarse fallback sin bloqueo.
5. Confirmar que se conserva la regla de no modificar sin autorización y respuesta en español MX.

**Decisiones acordadas**
- Prioridad: velocidad de respuesta, calidad técnica y cobertura de stack.
- Alcance: optimización balanceada, no disruptiva.
- Compatibilidad: flujo condicional (no plantilla obligatoria en todos los casos).
