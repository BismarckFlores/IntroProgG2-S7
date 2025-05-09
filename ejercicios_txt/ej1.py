"""1. Suma de los primeros N números
    o Enunciado: Pide al usuario un número entero positivo N y calcula la suma de los números desde 1 hasta N.
    o Especificación: Usa un bucle for y un acumulador."""

while True:
    try:
        num = int(input("Ingrese un número entero positivo: "))
        if num <= 0:
            print("Error. Ingrese un número positivo.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")

suma = 0

for i in range(1, num + 1):
    suma += i

print(f"La suma de los números del 1 al {num} es: {suma}")