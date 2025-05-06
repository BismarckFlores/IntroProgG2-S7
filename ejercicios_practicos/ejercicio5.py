""". Factorial de un número
    o Enunciado: Pide al usuario un número entero positivo y calcula su factorial.
    o Especificación: Usa un bucle while y un acumulador (para el producto)."""

def factorial(num):
    fact = 1            #Acumulador para el producto
    i = 1               #Contador
    while i <= num:
        fact *= i
        i += 1
    return fact

def main():
    num = int(input("Ingrese un número entero positivo: "))
    if num <= 0:
        print("Error. Ingrese un número válido")
    else:
        print(f"El factorial de {num} es: {factorial(num)}")

main()