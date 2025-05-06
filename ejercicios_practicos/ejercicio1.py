"""Suma de los primeros N números
    o Enunciado: Pide al usuario un número entero positivo N y calcula la suma de los números desde 1 hasta N.
    o Especificación: Usa un bucle for y un acumulador"""

num = int(input("ingrese un número entero positivo: "))
sum = 0

if num <= 0:
    print("Error. Ingrese un número válido")
else:
    for i in range(1, num +1):
        sum += i
    print(f"La suma de los números del 1 al {num} es: {sum}")