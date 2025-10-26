# Datos de Encuesta Egopolítica 2014 - 2025

## 🧠 Cómo usarlo en Power BI

- Exporta las tablas desde tu CSV como te mostré con el script en Python.
- Carga los 7 archivos CSV a Power BI.
- En el panel Modelado → Administrar relaciones, crea las relaciones:
    - Id_Encuesta de Encuestado → Id_Encuesta en cada tabla dependiente.
    - Cardinalidad: Uno a muchos (1:*).
- Usa Encuestado como tabla principal para segmentaciones (edad, sexo, región, etc.) y las demás tablas para crear medidas o visualizaciones específicas.
