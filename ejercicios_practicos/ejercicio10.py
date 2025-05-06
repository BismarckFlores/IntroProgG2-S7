"""Simulación de un cajero automático (simplificado)
    o Enunciado: Simula un cajero automático con un saldo inicial. Permite al usuario realizar depósitos (sumar al saldo) y retiros (restar del saldo) hasta que decida salir.
        Muestra el saldo actual en cada operación.
    o Especificación: Usa un bucle while, un acumulador (para el saldo), y contadores (opcionales, para el número de depósitos/retiros)"""


saldo = 1000.0
depositos = 0
retiros = 0
while True:
    print("="*15,"Cajero automático", "="*15)
    print("1. Depositar")
    print("2. Retirar")
    print("3. Salir")
    opcion = input("Seleccione una opción (1-3): ")
    match opcion:
        case "1":   #Deposito
            monto = float(input("Ingrese el monto a depositar: "))
            if monto > 0:
                saldo += monto
                depositos += 1
                print(f"Depósito exitoso. Saldo actual: ${saldo:.2f}")
            else:
                print("Monto inválido")
        case "2":   #Retiro
            monto = float(input("Ingrese el monto a retirar: "))
            if monto > 0 and monto <= saldo:
                saldo -= monto
                retiros += 1
                print(f"Retiro exitoso. Saldo actual: ${saldo:.2f}")
            else:
                print("Monto inválido")
        case "3":
            print("\nSaliendo del cajero...")
            print(f"Saldo final: ${saldo:.2f}")
            print(f"Total de depósitos: {depositos}")
            print(f"Total de retiros: {retiros}")
            break
        case _:
            print("Opción inválida. Intente nuevamente.")