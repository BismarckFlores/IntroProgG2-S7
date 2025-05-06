"""Leer una palabra diferente a fin y convertirla a mayuscula"""

for palabra in iter(input, "fin"):
    print(f"{palabra.capitalize()} tiene {len(palabra)} letras")
else:
    print("Termino...")