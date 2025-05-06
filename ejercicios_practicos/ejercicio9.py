"""Calcular la frecuencia de cada dígito en un número
    o Enunciado: Pide al usuario un número entero y calcula cuántas veces aparece cada dígito (0 al 9) en el número.
    o Especificación: Usa un bucle while y un array/list de contadores (uno para cada dígito)"""

def contador(numero):
    frecuencias = [0] * 10      #Lista de 10 contadores, uno por cada dígito (0-9)
    numero = abs(numero)        #Asegurar que el número sea positivo
    if numero == 0:
        frecuencias[0] = 1
    else:
        while numero > 0:
            digito = numero % 10
            frecuencias[digito] += 1
            numero //= 10
    return frecuencias

def main():
    num = int(input("Ingrese un número entero: "))
    frecuencias = contador(num)
    print("Frecuencia de cada dígito: ")
    for i in range(10):
        print(f"{i}: {frecuencias[i]}")

main()