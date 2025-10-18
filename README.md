# Agente Médico

Una aplicación web que utiliza procesamiento de lenguaje natural y búsquedas en línea para proporcionar diagnósticos preliminares y recomendaciones de medicamentos basados en descripciones de síntomas.

## Características

- **Procesamiento de Lenguaje Natural**: Utiliza spaCy para analizar y extraer síntomas de descripciones en español.
- **Búsqueda en Google**: Integra búsquedas seguras en Google para obtener información médica.
- **Diagnósticos Preliminares**: Genera posibles diagnósticos basados en síntomas identificados.
- **Recomendaciones de Medicamentos**: Sugiere tratamientos farmacológicos de fuentes confiables.
- **Interfaz Intuitiva**: Construida con Streamlit para una experiencia de usuario sencilla.
- **Advertencias Médicas**: Incluye disclaimers importantes sobre el uso responsable.

## Instalación

1. Clona el repositorio o descarga los archivos.
2. Instala las dependencias:
   ```
   pip install streamlit requests beautifulsoup4 googlesearch-python spacy
   ```
3. Descarga el modelo de spaCy para español:
   ```
   python -m spacy download es_core_news_sm
   ```

## Uso

Ejecuta la aplicación con:

```
streamlit run app.py
```

Abre el navegador en la URL proporcionada (generalmente http://localhost:8501) e ingresa una descripción de síntomas.

## Advertencias Importantes

⚠️ **Esta aplicación es solo para fines informativos y educativos. No reemplaza la consulta médica profesional.**

- Los diagnósticos generados son preliminares y pueden no ser precisos.
- Las recomendaciones de medicamentos deben ser verificadas por un médico calificado.
- No utilice esta aplicación para autodiagnóstico o automedicación.
- Consulte siempre a un profesional de la salud para cualquier condición médica.

## Tecnologías Utilizadas

- **Streamlit**: Framework para aplicaciones web.
- **spaCy**: Biblioteca de procesamiento de lenguaje natural.
- **googlesearch-python**: Para búsquedas en Google.
- **BeautifulSoup**: Para extracción de texto de páginas web.
- **Requests**: Para solicitudes HTTP.

## Limitaciones

- La precisión depende de la calidad de la información disponible en línea.
- No maneja casos complejos o emergencias médicas.
- Requiere conexión a internet para funcionar.
- Los resultados pueden variar según la disponibilidad de información.

## Contribución

Si deseas contribuir, por favor crea un issue o pull request en el repositorio.

## Licencia

Este proyecto es de código abierto. Consulta el archivo de licencia para más detalles.
