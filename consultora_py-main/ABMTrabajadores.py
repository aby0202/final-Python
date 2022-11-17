from validaciones import validarIngresoEntero

def obtenerTrabajadores(nombreArchivo):
  try:
    archivo = open(nombreArchivo,"r")
  except FileNotFoundError:
    archivo = open(nombreArchivo,"a")
    archivo.write("1,Esteban,21,34567567,Programador,true")
    archivo.close()
    archivo = open(nombreArchivo,"r")

#Nombre,edad,dni,profesion,activo(true,false)


  trabajadores=[]
  for linea in archivo.readlines():
    trabajador=linea.replace('\n','') # "6Gato34"
    trabajador=trabajador.split(",") # ["6Gato34"]
    trabajador = {"codigo":int(trabajador[0]),"nombre":trabajador[1],"edad":int(trabajador[2]),"dni":int(trabajador[3]),"profesion":trabajador[4],"activo":trabajador[5]}
    trabajadores.append(trabajador)
  archivo.close()
  return trabajadores


def agregarTrabajador(listado):
  codigo = validarIngresoEntero("codigo: ")
  nombre=input("nombre: ")
  edad = validarIngresoEntero("Edad: ")
  dni=validarIngresoEntero("dni: ")
  profesion=input("profesion: ")
  activo=input("activo: ")#aca no se si poner bool porque debo pasar true o false, si pongo bool ni siquiera me aparece para completar

  # Crea al trabajador y lo guarda en el listado
  trabajador = {"codigo":codigo,"nombre":nombre, "edad":edad, "dni":dni, "profesion":profesion, "activo":activo}
  listado.append(trabajador)

  # Agrega al trabajador a el archivo
  archivo = open("trabajadores.dat","a")
  linea = f"\n{codigo},{trabajador['nombre']},{trabajador['edad']},{trabajador['dni']},{trabajador['profesion']},{trabajador['activo']}"
  archivo.write(linea)
  archivo.close()





def modificarTrabajador(listado, codigo):
  for trabajador in listado:
    if trabajador["codigo"] == codigo:
      print(trabajador)
      nombre = input("Nombre: (Presiona Enter para no modificar) ")
      if nombre == "":
        nombre = trabajador["nombre"]
      
      edad = validarIngresoEntero("Edad: ")
      profesion=input("profesion: ")
      activo=input("activo: ")#activo o status? como decia por aca hay q pasar true o false ,hay q buscar la forma

      # Grabar en listado las modificaciones
      trabajador["nombre"] = nombre
      trabajador["edad"] = edad
      trabajador["profesion"] = profesion
      trabajador["activo"]=activo
      break



def modificarStatusTrabajador(listado, dni):
  for trabajador in listado:
    if trabajador["dni"] == dni:
      print(trabajador)
      activo = input("Activo: (Presiona Enter para no modificar) ")
      if activo == "":
        activo = trabajador["activo"]
      
      # Grabar en listado las modificaciones
      trabajador["activo"]=activo
      break




  # Grabar en archivo
  archivo = open("trabajadores.dat","w")
  contenido = []
  for empleadito in listado:
    linea = f"\n{empleadito['codigo']},{empleadito['nombre']},{empleadito['edad']},{empleadito['dni']},{empleadito['profesion']},{empleadito['activo']}"
    contenido.append(linea)

  contenido[0] = contenido[0].replace("\n","")
  archivo.writelines(contenido) 

  archivo.close()




def eliminarTrabajador(listado, codigo):
  indice=0
  for trabajador in listado:
    if trabajador["codigo"] == codigo:
      print(trabajador)
      listado.pop(indice)
      #creo que el pop te devolvia el valor
      break
    indice = indice + 1

  print(listado) 


  
  # Eliminar en archivo

  archivo = open("trabajadores.dat","w")
  contenido = []
  for empleadito in listado:
    linea = f"\n{empleadito['codigo']},{empleadito['nombre']},{empleadito['edad']},{empleadito['dni']},{empleadito['profesion']},{empleadito['activo']}"
    contenido.append(linea)

  contenido[0] = contenido[0].replace("\n","")
  archivo.writelines(contenido) 

  archivo.close()

