from dotenv import load_dotenv
load_dotenv()

import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

def generar_respuesta(email_cliente, nombre_empresa, firma):
    resp = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=600,
        system=f"""Eres un asistente de servicio al cliente profesional de {nombre_empresa}.
Tu tarea es:
1. Analizar el correo del cliente
2. Identificar: tono (molesto/neutro/positivo), problema principal, urgencia
3. Generar una respuesta profesional, empática y en español
4. La respuesta debe resolver o dar siguiente paso claro

Firma siempre con: {firma}""",
        messages=[{
            "role": "user",
            "content": f"Correo del cliente:\n\n{email_cliente}"
        }]
    )
    return resp.content[0].text

# ── Casos de prueba ────────────────────────────
emails = [
    """Llevan 3 días sin resolver mi problema de facturación. 
    Me cobraron doble en enero y nadie me da respuesta. 
    Si no resuelven hoy cancelo mi suscripción.""",

    """Hola, quería preguntar si tienen plan anual con descuento. 
    Estoy muy contento con el servicio, solo quiero optimizar costos.""",

    """Buenos días, necesito una factura del mes pasado 
    para mi declaración fiscal. ¿Me pueden ayudar?"""
]

empresa = "TechMex Soluciones"
firma = "Equipo de Atención al Cliente\nTechMex Soluciones\nTel: 55-1234-5678"

for i, email in enumerate(emails, 1):
    print(f"\n{'='*55}")
    print(f"EMAIL #{i}")
    print(f"{'='*55}")
    print(f"CLIENTE: {email[:80]}...")
    print(f"\nRESPUESTA GENERADA:")
    print(generar_respuesta(email, empresa, firma))