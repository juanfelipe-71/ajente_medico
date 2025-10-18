#!/bin/bash
# Script de configuración para Streamlit Cloud

echo "Descargando modelo de spaCy para español..."
python -m spacy download es_core_news_sm

echo "Verificando instalación..."
python -c "import spacy; nlp = spacy.load('es_core_news_sm'); print('Modelo cargado correctamente')"

echo "Configuración completada"