"""Promedio de N calificaciones
    o Enunciado: Pide al usuario la cantidad N de calificaciones y luego solicita cada calificación. Calcula el promedio de las calificaciones ingresadas.
    o Especificación: Usa un bucle for para leer las calificaciones, un acumulador para la suma, y un contador para la cantidad."""

def promedio(n):
    calificaciones = []
    for i in range(n):
        cal = float(input(f"Ingrese la calificación {i+1}: "))
        calificaciones.append(cal)
    prom = sum(calificaciones) / n
    return prom, calificaciones

def main():
    n = int(input("¿Cuántas calificaciones desea ingresar? "))
    if n <= 0:
        print("Error. Ingrese un número válido")
    else:
        prom, cal = promedio(n)
        print("Calificaciones ingresadas:", cal)
        print(f"El promedio es: {prom}")

main()