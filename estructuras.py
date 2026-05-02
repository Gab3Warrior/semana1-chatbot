# ─── LISTAS ───────────────────────────────────────────────────
frutas = ["mango", "papaya", "guayaba", "tamarindo"]

print("Lista completa:", frutas)
print("Primera fruta:", frutas[0])
print("Última fruta:", frutas[-1])

frutas.append("mamey")
print("Con mamey:", frutas)

# ─── DICCIONARIOS ─────────────────────────────────────────────
perfil = {
    "nombre": "Gab",
    "ciudad": "CDMX",
    "skills": ["Python", "IA", "Crypto"],
    "meta": "independencia financiera"
}

print("\nNombre:", perfil["nombre"])
print("Skills:", perfil["skills"])

for clave, valor in perfil.items():
    print(f"  {clave}: {valor}")

# ─── ARCHIVOS ─────────────────────────────────────────────────
with open("mi_perfil.txt", "w") as f:
    for clave, valor in perfil.items():
        f.write(f"{clave}: {valor}\n")

print("\nArchivo guardado.")

with open("mi_perfil.txt", "r") as f:
    contenido = f.read()
    print("\nContenido del archivo:")
    print(contenido)