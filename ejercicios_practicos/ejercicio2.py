"""Producto de los primeros M números pares
    o Enunciado: Pide al usuario un número entero positivo M y calcula el producto de los primeros M números pares.
    o Especificación: Usa un bucle while, un acumulador (para el producto), y un contador"""

def bucle(m):
    prod = 1            #Acumulador para el producto
    cont = 0            #Contador de números pares usados
    num_par = 2         #Primer numero par
    while cont < m:
        prod *= num_par
        cont += 1
        num_par += 2    #Avanza al siguiente numero par
    return f"El producto de los primeros {m} números pares es: {prod}"

def main():
    m = int(input("Ingrese un número entero positivo: "))
    if m <= 0:
        print("Error. Ingrese un número válido.")
    else:
        print(bucle(m))

main()