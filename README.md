# 🤖 Semana 1 — Automatización con IA

Proyectos construidos durante la primera semana del plan de aprendizaje
en IA, Seguridad y Crypto orientado a independencia financiera.

## Proyectos

### 💬 Chatbot de Soporte al Cliente
Asistente conversacional con memoria, personalidad configurable y
guardado automático de conversaciones.
- **Archivo:** `chatbot_negocio.py`
- **Tecnología:** Python + Claude API
- **Uso:** Cambia las variables NEGOCIO, TIPO y GUION para adaptarlo a cualquier cliente

### 🎫 Extractor de Tickets
Analiza mensajes de clientes y extrae nombre, problema, urgencia
y acción recomendada en formato JSON estructurado.
- **Archivo:** `extractor.py`
- **Tecnología:** Python + Claude API + JSON

### 📧 Generador de Respuestas de Email
Genera respuestas profesionales y empáticas para correos de clientes,
adaptando el tono según la urgencia detectada.
- **Archivo:** `respuestas_email.py`
- **Tecnología:** Python + Claude API

### 🌤️ Consulta de Clima
Integración con API pública para obtener clima en tiempo real.
- **Archivo:** `clima.py`
- **Tecnología:** Python + requests

## Instalación

git clone https://github.com/Gab3Warrior/semana1-chatbot.git
cd semana1-chatbot
pip3 install anthropic python-dotenv requests

Crea un archivo .env con tu API key:

ANTHROPIC_API_KEY=tu-key-aqui

## Stack

- Python 3.12
- Anthropic Claude API (Haiku)
- python-dotenv
- requests

## Autor

**Gab** · Ciudad de México  
[GitHub](https://github.com/Gab3Warrior)