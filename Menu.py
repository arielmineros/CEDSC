import switch
import os

# Creación del menú
while True:
    #Limpieza de pantalla
    #os.system("cls") 
    os.system("clear")
    print("1. Añadir un C.E \n2. Ver todos los C.E. \n3. Actualizar un C.E. \n4. Eliminar un C.E. \n5. Salir")
    option = int(input("\nIngrese la opción: "))
    if option == 5:
        break
    switch.switch_option(option)
    continue
