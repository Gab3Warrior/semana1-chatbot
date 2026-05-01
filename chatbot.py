import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
historial = []

print("Asistente listo. Escribe 'salir' para terminar.\n")

while True:
    user_input = input("Tú: ")
    if user_input.lower() == "salir":
        print("¡Hasta luego!")
        break
    
    historial.append({"role": "user", "content": user_input})
    
    resp = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        system="Eres un asistente técnico amigable que responde en español.",
        messages=historial
    )
    
    reply = resp.content[0].text
    historial.append({"role": "assistant", "content": reply})
    print(f"\nAsistente: {reply}\n")