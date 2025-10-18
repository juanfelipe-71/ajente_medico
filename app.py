import streamlit as st
import spacy
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
import google.generativeai as genai
import os
from tavily import TavilyClient
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar APIs desde variables de entorno
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# Cargar modelo de spaCy para español (con manejo de errores)
try:
    nlp = spacy.load('es_core_news_sm')
except OSError:
    st.error("Error: No se pudo cargar el modelo de lenguaje español. Ejecutando descarga...")
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "es_core_news_sm"])
    nlp = spacy.load('es_core_news_sm')

# Función para buscar en Google (con manejo de rate limiting)
def buscar_en_google(query, num_results=3):
    try:
        import time
        time.sleep(2)  # Pausa para evitar rate limiting
        results = list(search(query, num_results=num_results, lang='es'))
        return results
    except Exception as e:
        if "429" in str(e):
            st.warning("Demasiadas solicitudes. Intenta usar el método de IA Avanzada o espera unos minutos.")
            return []
        st.error(f"Error en la búsqueda: {e}")
        return []

# Función para buscar con Tavily (más confiable)
def buscar_con_tavily(query):
    try:
        response = tavily_client.search(query, search_depth="advanced")
        return [result['url'] for result in response['results'][:3]]  # Reducido a 3 para optimizar
    except Exception as e:
        st.error(f"Error en búsqueda Tavily: {e}")
        return []

# Función para generar diagnóstico con Gemini AI
def generar_diagnostico_ai(sintomas, descripcion):
    try:
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        prompt = f"""
        Basado en los siguientes síntomas identificados: {', '.join(sintomas)}
        Y la descripción completa: {descripcion}

        Proporciona 3-5 posibles diagnósticos médicos preliminares.
        Para cada diagnóstico, incluye:
        - Nombre de la condición
        - Breve explicación
        - Nivel de probabilidad (bajo, medio, alto)

        IMPORTANTE: Recuerda que esto es solo informativo y no reemplaza consulta médica profesional.
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error con Gemini AI: {e}")
        return "No se pudo generar diagnóstico con IA."

# Función para recomendar medicamentos con Gemini AI
def recomendar_medicamentos_ai(diagnostico, sintomas):
    try:
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        prompt = f"""
        Para el diagnóstico preliminar: {diagnostico}
        Con síntomas: {', '.join(sintomas)}

        Recomienda medicamentos comunes de fuentes confiables como:
        - Analgésicos
        - Antiinflamatorios
        - Antibióticos (solo si aplica)
        - Otros tratamientos sintomáticos

        Para cada medicamento incluye:
        - Nombre
        - Dosis típica
        - Precauciones importantes

        IMPORTANTE: Estas son recomendaciones generales. Consulte a un médico antes de tomar cualquier medicamento.
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error con Gemini AI: {e}")
        return "No se pudieron generar recomendaciones."

# Función para extraer texto de una URL
def extraer_texto(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extraer texto del cuerpo
        texto = soup.get_text()
        return texto
    except Exception as e:
        return f"Error al extraer texto: {e}"

# Función para procesar síntomas con NLP
def procesar_sintomas(descripcion):
    doc = nlp(descripcion)
    sintomas = [token.lemma_ for token in doc if token.pos_ in ['NOUN', 'ADJ'] and not token.is_stop]
    return sintomas

# Función para generar diagnóstico basado en búsqueda (método alternativo)
def generar_diagnostico_tradicional(sintomas):
    query = "diagnóstico médico para " + " ".join(sintomas)
    urls = buscar_en_google(query)
    diagnosticos = []
    for url in urls[:3]:  # Limitar a 3 resultados
        texto = extraer_texto(url)
        # Buscar patrones de diagnóstico en el texto
        patrones = re.findall(r'(?:diagnóstico|posible causa|enfermedad).*?([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', texto, re.IGNORECASE)
        diagnosticos.extend(patrones)
    return list(set(diagnosticos))[:5]  # Limitar a 5 diagnósticos únicos

# Función para recomendar medicamentos (método alternativo)
def recomendar_medicamentos_tradicional(diagnostico):
    query = f"medicamentos para {diagnostico} fuentes confiables"
    urls = buscar_en_google(query)
    medicamentos = []
    for url in urls[:3]:
        texto = extraer_texto(url)
        # Buscar medicamentos comunes
        patrones = re.findall(r'(?:medicamento|tratamiento).*?([A-Z][a-z]+(?:\s+[a-z]+)*)', texto, re.IGNORECASE)
        medicamentos.extend(patrones)
    return list(set(medicamentos))[:5]

# Interfaz de Streamlit
st.title("Agente Médico - Diagnóstico y Recomendaciones")
st.warning("⚠️ Esta aplicación es solo para fines informativos. No reemplaza la consulta médica profesional. Consulte a un médico para diagnósticos precisos.")

# Selector de método
metodo = st.radio("Método de análisis:", ["IA Avanzada (Gemini + Tavily)", "Búsqueda Web Tradicional"], key="metodo_selector")

# Información sobre métodos
if metodo == "IA Avanzada (Gemini + Tavily)":
    st.info("💡 Este método utiliza IA de Google Gemini y búsquedas avanzadas de Tavily para diagnósticos más precisos.")
else:
    st.info("💡 Este método utiliza búsquedas tradicionales en Google. Puede estar limitado por políticas de uso.")

descripcion = st.text_area("Describe tus síntomas o la enfermedad:", height=150, key="descripcion_input")

# Contenedor para resultados
result_container = st.container()

if st.button("Analizar", key="analizar_button"):
    if descripcion.strip():
        with result_container:
            with st.spinner("Procesando..."):
                sintomas = procesar_sintomas(descripcion)
                st.subheader("Síntomas identificados:")
                st.write(", ".join(sintomas))

                if metodo == "IA Avanzada (Gemini + Tavily)":
                    # Usar Gemini AI para diagnóstico
                    diagnostico_ai = generar_diagnostico_ai(sintomas, descripcion)
                    st.subheader("Diagnóstico generado por IA:")
                    st.markdown(diagnostico_ai)

                    # Recomendaciones con IA
                    medicamentos_ai = recomendar_medicamentos_ai(diagnostico_ai.split('\n')[0], sintomas)
                    st.subheader("Recomendaciones de medicamentos (IA):")
                    st.markdown(medicamentos_ai)

                else:
                    # Método tradicional
                    diagnosticos = generar_diagnostico_tradicional(sintomas)
                    if diagnosticos:
                        st.subheader("Posibles diagnósticos:")
                        for diag in diagnosticos:
                            st.markdown(f"- {diag}")
                    else:
                        st.write("No se encontraron diagnósticos sugeridos.")

                    if diagnosticos:
                        medicamentos = recomendar_medicamentos_tradicional(diagnosticos[0])
                        if medicamentos:
                            st.subheader("Medicamentos sugeridos:")
                            for med in medicamentos:
                                st.markdown(f"- {med}")
                        else:
                            st.write("No se encontraron recomendaciones de medicamentos.")
    else:
        st.error("Por favor, describe tus síntomas.")

# Botón para nueva consulta
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔄 Nueva Consulta", key="nueva_consulta", help="Limpiar resultados y hacer una nueva consulta"):
        st.rerun()

st.markdown("---")
st.caption("Desarrollado con Streamlit, Gemini AI y Tavily. Información basada en búsquedas web e IA.")