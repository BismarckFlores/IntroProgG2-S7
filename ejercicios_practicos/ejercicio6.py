"""Contar palabras en una frase
    o Enunciado: Pide al usuario una frase y cuenta el número de palabras que contiene.
    o Especificación: Usa un bucle for (o métodos de string) y un contador. """

def contador(cadena):
    palabras = cadena.split()
    return len(palabras)

def main():
    frase = input("Ingrese una frase: ")
    print(f"La frase ingresada contiene {contador(frase)} palabras")

main()