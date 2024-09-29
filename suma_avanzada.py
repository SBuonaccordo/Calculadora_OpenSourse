def suma_avanzada(num1, num2):
    resultado = num1 + num2
    print("\n==========\n")
    print(resultado)
    print("\n==========\n")

    while True:
        continuar = input("¿Quieres sumar otro número? (si/no): ").strip().lower()

        if continuar == 'si':
            nuevo_numero = float(input("Ingresa otro número: "))
            resultado += nuevo_numero
            print("\n==========\n")
            print(resultado)
            print("\n==========\n")
        elif continuar == 'no':
            break
        else:
            print("Por favor, responde con 'si' o 'no'.")
