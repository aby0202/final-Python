def menuPrincipal():
    print(
        f''' 
        \t Bienvenido al Sistema de Gestion de Personal

        Seleccione una opcion
        
        [1] Gestion de trabajadores
        [2] Reportes
        [3] Cambiar estado del trabajador
        [0] Salir
        '''
        )



def menuGestionTrabajador():
    print(
        f'''
            \t Gestion de trabajadores 

            Seleccione una opcion

            [1] Ingresar nuevo trabajador
            [2] Modificar dato de trabajador
            [3] Eliminar trabajador
            [0] Volver al menu principal
            '''
        )

def menuReportes():
    print(
        f'''
         \t Reportes

         Seleccione una opcion

         [1] Mostrar trabajadores activos
         [2] Mostrar personas desocupadas
         [3] Mostrar desocupados por rango de edad
         [4] Mostrar trabajadores segun profesion
         [0] Volver al menu principal
        '''
    )

def menuActualizarEstadoDelTrabajador():
    print(
        f'''
            \t Actualizar estado del trabajador

            Seleccione una opcion

            [1]Buscar trabajador segun DNI
            [0]Volver al menu principal
        '''
    )