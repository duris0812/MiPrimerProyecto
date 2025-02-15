#Calculadora
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else "Error: División por cero"

operaciones = {
    '1': ('Suma', suma),
    '2': ('Resta', resta),
    '3': ('Multiplicación', multiplicacion),
    '4': ('División', division),
}

def calculadora():
    while True:
        print("\nSeleccione operación:")
        for key, (nombre, _) in operaciones.items():
            print(f"{key}. {nombre}")
        print("5. Salir")

        opcion = input("Ingrese opción (1/2/3/4/5): ")

        if opcion == '5':
            print("Saliendo...")
            break

        if opcion not in operaciones:
            print("Opción no válida. Intente de nuevo.")
            continue

        try:
            num1 = float(input("Ingrese primer número: "))
            num2 = float(input("Ingrese segundo número: "))
            _, operacion = operaciones[opcion]
            print("Resultado:", operacion(num1, num2))
        except ValueError:
            print("Error: Entrada no válida. Ingrese números.")

calculadora()
