"""Suma de números pares e impares
    o Enunciado: Pide al usuario una lista de números (pueden ser ingresados uno a la vez hasta que el usuario ingrese un valor de fin, como 0 o -1). Calcula la suma de
    los números pares y la suma de los números impares.
    o Especificación: Usa un bucle while, acumuladores para la suma de pares e impares, y un contador (opcional, dependiendo de la implementación)."""

def suma(num):
    sum_pares = 0
    sum_impares = 0
    while num != 0:
        if num % 2 == 0:
            sum_pares += num
        else:
            sum_impares += num
        num = int(input("Ingresa otro número (0 para terminar): "))
    return sum_pares, sum_impares

def main():
    num = int(input("Ingresa un número (0 para terminar): "))
    suma_p, suma_i = suma(num)
    print(f"Suma de números pares: {suma_p}")
    print(f"Suma de números impares: {suma_i}")

main()