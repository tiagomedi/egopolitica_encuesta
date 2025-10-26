# Datos de Encuesta Egopolítica 2014 - 2025

## 🧠 Cómo usarlo en Power BI
- Carga los 7 archivos CSV a Power BI.
- En el panel Modelado → Administrar relaciones, crea las relaciones:
    - Id_Encuesta de Encuestado → Id_Encuesta en cada tabla dependiente.
    - Cardinalidad: Uno a muchos (1:*).
- Usa Encuestado como tabla principal para segmentaciones (edad, sexo, región, etc.) y las demás tablas para crear medidas o visualizaciones específicas.

## 🧭 Te explico paso a paso cómo hacerlo:
- Importa todas las tablas CSV que generaste (por ejemplo: Encuestado.csv, Percepciones.csv, etc.).
    - En Power BI: → Inicio → Obtener datos → Texto/CSV → seleccionas cada archivo.
- Una vez importadas todas las tablas:
    - Ve a la vista “Modelado” (ícono de tres recuadros conectados, normalmente a la izquierda).
- En el panel “Administrar relaciones”:
    - Haz clic en “Nueva”.
    - Selecciona la tabla principal (Encuestado) y el campo Id_Encuesta.
    - Luego selecciona la tabla relacionada (por ejemplo Percepciones) y también el campo Id_Encuesta.
- Configura la relación:
    - Cardinalidad: “Uno a varios (1:*)”
    - Dirección del filtro cruzado: “Ambos” o “Único → Relacionada” (depende del análisis).
    - Presiona Aceptar.
- Repite esto para cada tabla dependiente:
    - Evaluaciones_Politicas
    - Confianza_Instituciones
    - Democracia
    - Bienestar
    - Estallido_Social
    - Percepciones
