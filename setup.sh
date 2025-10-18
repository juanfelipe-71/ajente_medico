#!/bin/bash
# Script de configuración para Streamlit Cloud

echo "Descargando modelo de spaCy para español..."
python -m spacy download es_core_news_sm

echo "Verificando instalación..."
python -c "
try:
    import spacy
    nlp = spacy.load('es_core_news_sm')
    print('Modelo cargado correctamente')
except Exception as e:
    print(f'Error al cargar modelo: {e}')
    print('Intentando descarga alternativa...')
    import subprocess
    subprocess.run(['python', '-m', 'spacy', 'download', 'es_core_news_sm'], check=True)
    print('Descarga completada')
"

echo "Configuración completada"