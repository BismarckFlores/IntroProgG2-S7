"""Contar vocales en una cadena
    o Enunciado: Pide al usuario una cadena y cuenta cuántas vocales (a, e, i, o, u) tiene.
    o Especificación: Usa un bucle for para recorrer la cadena y contadores para cada """

def contador(cadena):
    vocales = ["a", "e", "i", "o", "u"]
    total = 0
    for char in cadena.lower():
        if char in vocales:
            total += 1
    return total

def main():
    cadena = input("Ingrese un enunciado: ")
    print(f"La cadena contiene {contador(cadena)} vocales")

main()