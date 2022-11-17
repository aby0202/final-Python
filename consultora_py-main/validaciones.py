def validarIngresoEntero(opcion):
    while True:
        try:
            entero = int(input(opcion))
            break
        except ValueError:
            print("El valor ingresado no es un numero. Reintente")
    return entero
