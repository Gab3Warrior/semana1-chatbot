from dotenv import load_dotenv
load_dotenv()

import anthropic
import os

# ─── CONFIGURACIÓN DEL NEGOCIO ───────────────────────────────
NEGOCIO = "Tienda de tecnología TechMex"
TIPO = "soporte técnico"
GUION = """
- Ayudas a clientes con problemas de computadoras, celulares y accesorios
- Si el problema requiere revisión física, agenda una cita
- Horario de atención: lunes a sábado 9am - 7pm
- Dirección: Av. Insurgentes 123, CDMX
- Si no sabes la respuesta, di: "Permíteme consultarlo con un especialista"
"""
# ─────────────────────────────────────────────────────────────

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
historial = []

SYSTEM_PROMPT = f"""
Eres el asistente virtual de {NEGOCIO}, especializado en {TIPO}.
Responde siempre en español, con tono amable y profesional.
Guión de atención:
{GUION}
Si el cliente se despide, ofrece un resumen de lo que se resolvió.
"""

print(f"\n{'='*50}")
print(f"  Asistente de {TIPO} — {NEGOCIO}")
print(f"{'='*50}")
print("Escribe 'salir' para terminar.\n")

while True:
    user_input = input("Cliente: ")
    if user_input.lower() == "salir":
        print("\nAsistente: ¡Gracias por contactarnos! Que tenga buen día. 😊")
        with open("conversacion.txt", "w") as f:
            for msg in historial:
                rol = "Cliente" if msg["role"] == "user" else "Asistente"
                f.write(f"{rol}: {msg['content']}\n\n")
        print("Conversación guardada en conversacion.txt")
        break

    historial.append({"role": "user", "content": user_input})

    resp = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        system=SYSTEM_PROMPT,
        messages=historial
    )

    reply = resp.content[0].text
    historial.append({"role": "assistant", "content": reply})
    print(f"\nAsistente: {reply}\n")