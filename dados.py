guion = "="
print(guion * 80)
print("Bienvenidos a mi programa")
print( guion * 80)
#============================================================
nombre = input("Por favor ingrese su nombre: ")
direccion = input("Por favor ingrese su direccion: ")
correo = input("Por favor ingrese su correo electronico: ")
telefono = int(input("Por favor ingrese su telefono de contacto: "))
ocupacion = input("Por favor ingrese su ocupacion: ")
#==============================================================
nombre_2 = f" Hola {nombre}, Felicidades por su compra, ha sido seleccionado participante para un premio"
direccion_2 = f"Le enviaremos el premio a la siguiente direccion: {direccion}"
correo_2 = f"Le estaremos notificando las actualizaciones al correo {correo}"
telefono_2 = f"Le estaremos contactando al numero de telefono agregado el cual es: {telefono}"
ocupacion_2 = f"Gracias a que su ocupacion es {ocupacion}"
#==============================================================
print(nombre_2)
print(direccion_2)
print(correo_2)
print(telefono_2)
print(ocupacion_2)
#==============================================================
print("")
print(guion * 80)
print("Gracias por usar mi codigo, me esforcé")
print(guion * 80)

guion = "="
print (guion * 60)
print ("BIENVENIDOS A MI PROGRAMA DE CALCULO")
print(guion * 60)
stack = """
EN ESTE PROGRAMA PODRAS:
- SUMAR.
- RESTAR.
- MULTIPLICAR.
- DIVIDIR.
Sin ningun inconvenientes y al tanto de tus necesidades.
"""
print()
numero1 = int(input("Por favor ingrese el primer numero a sumar: "))
numero2 = int(input("Por favor ingrese el segundo numero a sumar: "))
resultado_suma = numero1 + numero2 
print(f"El resultado de la suma es igtual a: {resultado_suma}")
# =========================================================================
numero_resta = int(input("Por favor ingrese el primer numero a restar: "))
numero_resta2 = int(input("Por favor ingrese el segundo numero a resta: "))
resultado_resta = numero_resta - numero_resta2
print(f"EL resultado de la resta es: {resultado_resta}")
# =========================================================================
numero_multi = int(input("Por favor ingrese el primer numero a multiplicar: "))
numero_multi2 = int(input("Por favor ingrese el segundo numero a multiplicar:"))
resultado_multi = numero_multi * numero_multi2
print(f"El resultado de la multiplicación es: {resultado_multi}")
#==========================================================================
numero_divi = int(input("Por favor ingrese el numero a dividir: "))
numero_divi2 = int(input("Por favor ingrese el numero a dividir: "))
resultado_divi = numero_divi / numero_divi2
print(f"El resultado de la división es: {resultado_divi}")
#=========================================================================
print()
print(guion * 60)
print("AQUI FINALIZA EL PROGRAMA DE CALCULO MUCHAS GRACIAS POR UTILIZARLO")
print(guion * 60) 


