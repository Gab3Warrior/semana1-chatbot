import anthropic
import os
import json

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

def extraer_info(texto):
    resp = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        system="""Eres un extractor de información. 
        Analiza el texto y responde SOLO con un JSON válido con esta estructura:
        {
            "nombre": "",
            "problema": "",
            "urgencia": "alta/media/baja",
            "accion": ""
        }
        Sin explicaciones, sin bloques de código, sin comillas, solo el JSON puro.""",
        messages=[{"role": "user", "content": texto}]
    )
    # Limpiar posibles comillas de código
    resultado = resp.content[0].text
    resultado = resultado.replace("```json", "").replace("```", "").strip()
    return resultado

# ─── CASOS DE PRUEBA ──────────────────────────────────────────
casos = [
    "Hola, soy María, mi computadora no enciende desde esta mañana y tengo una presentación en 2 horas",
    "Buenos días, quiero saber el precio del paquete premium, no hay prisa",
    "Soy Carlos, llevo 3 días sin internet y trabajo desde casa, necesito solución urgente"
]

resultados = []

for caso in casos:
    print(f"\nTexto: {caso[:50]}...")
    resultado = extraer_info(caso)
    print(f"Análisis: {resultado}")
    resultados.append(json.loads(resultado))

# Guardar resultados
with open("tickets.json", "w", encoding="utf-8") as f:
    json.dump(resultados, f, ensure_ascii=False, indent=2)

print("\n✅ Tickets guardados en tickets.json")