# APIs y Bibliotecas Utilizadas en Agente Médico

Este documento describe las APIs y bibliotecas externas utilizadas en la aplicación "Agente Médico".

## Bibliotecas Principales

### 1. Streamlit

- **Versión**: 1.40.2
- **Propósito**: Framework para crear aplicaciones web interactivas con Python.
- **Instalación**: `pip install streamlit`
- **Uso**: Construcción de la interfaz de usuario principal.
- **Documentación**: https://docs.streamlit.io/

### 2. spaCy

- **Versión**: 3.8.7
- **Propósito**: Biblioteca de procesamiento de lenguaje natural (NLP).
- **Modelo utilizado**: `es_core_news_sm` (para español).
- **Instalación**:
  ```
  pip install spacy
  python -m spacy download es_core_news_sm
  ```
- **Uso**: Análisis de texto para extraer síntomas de descripciones médicas.
- **Documentación**: https://spacy.io/

### 3. googlesearch-python

- **Versión**: 1.3.0
- **Propósito**: Biblioteca para realizar búsquedas en Google de manera programática.
- **Instalación**: `pip install googlesearch-python`
- **Uso**: Búsqueda web básica para información médica.
- **Limitaciones**: Sujeto a bloqueos de IP o cambios en los términos de servicio de Google.
- **Documentación**: https://pypi.org/project/googlesearch-python/

### 4. Requests

- **Versión**: 2.32.5
- **Propósito**: Biblioteca para hacer solicitudes HTTP.
- **Instalación**: `pip install requests`
- **Uso**: Descarga de contenido de páginas web para extracción de información.
- **Documentación**: https://requests.readthedocs.io/

### 5. BeautifulSoup4

- **Versión**: 4.14.2
- **Propósito**: Biblioteca para parsear documentos HTML y XML.
- **Instalación**: `pip install beautifulsoup4`
- **Uso**: Extracción de texto plano de páginas web médicas.
- **Documentación**: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

## APIs Externas

### Google Gemini AI

- **API Key**: AIzaSyAdYlV8Mo64GufUGFno4bJh9KE5sIY-rNA
- **Propósito**: Generación de diagnósticos médicos inteligentes y recomendaciones de medicamentos.
- **Biblioteca**: google-generativeai
- **Modelo utilizado**: gemini-2.0-flash-exp (experimental, compatible con generateContent)
- **Instalación**: `pip install google-generativeai`
- **Documentación**: https://ai.google.dev/docs
- **Uso**: Análisis avanzado de síntomas y generación de respuestas médicas contextuales.
- **Nota**: Modelo experimental actualizado para compatibilidad con la API v1beta.

### Tavily Search API

- **API Key**: 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
- **Propósito**: Búsqueda web avanzada y confiable para información médica.
- **Biblioteca**: tavily-python
- **Instalación**: `pip install tavily-python`
- **Documentación**: https://docs.tavily.com/
- **Uso**: Búsquedas más precisas y estructuradas de información médica.

### Búsqueda Google Tradicional

- **Biblioteca**: googlesearch-python
- **Propósito**: Búsqueda web básica como método alternativo.
- **Limitaciones**: Sujeto a bloqueos de IP o cambios en los términos de servicio de Google.
- **Consideraciones éticas**: El uso debe ser responsable y no violar términos de servicio.

## Dependencias Adicionales

- **altair**: Para visualizaciones (usado por Streamlit).
- **pandas**: Para manipulación de datos.
- **numpy**: Para operaciones numéricas.
- **click, rich, toml**: Utilidades de línea de comandos y formato.

## Configuración y Variables de Entorno

Actualmente, la aplicación no requiere variables de entorno específicas. Sin embargo, para producción, se recomienda:

- Configurar proxies si es necesario para búsquedas.
- Implementar caching para reducir llamadas a Google.
- Agregar manejo de errores más robusto para conexiones fallidas.

## Actualizaciones y Mantenimiento

- Verificar regularmente las versiones de las bibliotecas para actualizaciones de seguridad.
- Monitorear cambios en las políticas de Google para búsquedas automatizadas.
- Considerar alternativas como APIs médicas oficiales (ej. PubMed API) para mayor confiabilidad.

## Notas de Seguridad

- Las búsquedas web pueden exponer datos sensibles; implementar encriptación si es necesario.
- No almacenar información médica personal sin consentimiento.
- Cumplir con regulaciones como HIPAA o equivalentes locales para datos de salud.
