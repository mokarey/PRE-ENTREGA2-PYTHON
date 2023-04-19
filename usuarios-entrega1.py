#-- primera pre-entrega 
#-- cambios = posibilidad de finalizar el ciclo, redaccion del menu con numeros.

usuarios = {}
menu = ""

def programa():
  menu = input("iniciar sesion = 1 / registrarse = 2 / mostrar usuarios = 3 / salir.")
  if menu == "1":
      login()
  elif menu == "2":
    registro()
  elif menu == "3":
    mostrarUsuarios()
  elif menu == "salir":
     salida()
    

def registro():
    crearUsuario = input("Porfavor, seleccione un nombre de usuraio: ")

    if crearUsuario in usuarios:
        print("El usuario seleccionado ya esta en uso")
    else: 
      crearContraseña = input("Ahora, seleccione una contraseña: ")
      usuarios[crearUsuario] = crearContraseña
      print("Su usuario fue creado con exito!")

def login():
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña :")
    
    if usuario in usuarios and usuarios[usuario] == contraseña:
      print("Inicio de sesion correcto!")
    else:
      print("Usuario inexistente o contraseña incorrecta, porfavor intente nuevamente.")
      programa()

def mostrarUsuarios():
  print([usuarios])

def salida():
   while menu == "salir":
      break

programa()
