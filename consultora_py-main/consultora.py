from validaciones import validarIngresoEntero
from decoraciones import decorar
from ABMTrabajadores import agregarTrabajador,modificarTrabajador,obtenerTrabajadores, eliminarTrabajador,modificarStatusTrabajador
from menues import menuPrincipal, menuGestionTrabajador, menuReportes,menuActualizarEstadoDelTrabajador

listadoDePersonas = obtenerTrabajadores("trabajadores.dat")

while True:

    decorar()
    menuPrincipal()
    opcion = validarIngresoEntero("Ingrese una opcion: ")

    if opcion == 0:
        opcionSalir = input("Está seguro que desea salir? [S]i/[N]o: ")
        if opcionSalir == "S":
            print("Saliendo...")
            break
        elif opcionSalir == "N":
            continue
        else:
            print("La opcion no es correcta. Reintente")
            continue

    elif opcion == 1:
        decorar()
        while True:
            menuGestionTrabajador()
            opcionGestionTrabajador = validarIngresoEntero("Seleccione una opcion: ")

            if opcionGestionTrabajador == 0:
                break
            elif opcionGestionTrabajador == 1:
                print("Ingresar nuevo trabajador")
                agregarTrabajador(listadoDePersonas)
            elif opcionGestionTrabajador == 2:
                print("Modificar datos de trabajador")
                codigo=validarIngresoEntero("Codigo del trabajador a modificar: ")
                modificarTrabajador(listadoDePersonas,codigo)
            elif opcionGestionTrabajador == 3:
                print("Eliminar trabajador")
                codigo=validarIngresoEntero("codigo del trabajador a eliminar: ")
                eliminarTrabajador(listadoDePersonas,codigo)
            else:
                print("La opcion no es correcta. Reintente")
                continue

    elif opcion == 2:
        decorar()
        while True:
            menuReportes()
            opcionReportes = validarIngresoEntero("Seleccione una opcion: ")

            if opcionReportes == 0:
                break
            elif opcionReportes == 1:
                print("Mostrando reporte de trabajadores activos")
            elif opcionReportes == 2:
                print("Mostrando reporte de personas desocupadas")
            elif opcionReportes == 3:
                print("Mostrando reporte de desocupados por rango de edad")
            elif opcionReportes == 4:
                print("Mostrando reporte de trabajadores por profesion")
            else:
                print("La opcion ingresada no es valida. Reintente")
                continue

    elif opcion == 3:
        decorar()
        print("Actualizar estado del trabajador")
        while True:
            menuActualizarEstadoDelTrabajador()
            opcionActualizarEstadoDelTrabajador = validarIngresoEntero("Seleccione una opcion: ")

            if opcionActualizarEstadoDelTrabajador == 1:
                print("Modificar status del trabajador")
                dni=validarIngresoEntero("DNI del trabajador a modificar: ")
                modificarStatusTrabajador(listadoDePersonas,dni)
            # else len(f'{dni}') > 8:
            #     print("El DNI no tiene un formato correcto.")
            # print(opcionActualizarEstadoDelTrabajador == 1)#esto iria como validacion pero en otra parte?? aca hay que ver como pasar solo true o false
            elif opcionActualizarEstadoDelTrabajador == 0:
                break
            else:
                print("La opcion no es correcta, Reintente")
                continue

    else:
        print("La opcion ingresada no es correcta. Reintente")