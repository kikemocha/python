# Escribir un programa en python que nos permita hacer una pequeña agenda. El
# programa debería de presentar un pequeño menú con cuatro opciones: dar de alta un
# contacto pulsando el 1, buscar un contacto, pulsando el 2, eliminar un contacto
# pulsando el 3 y salir pulsando el 0. Cualquier otro valor no debería de hacer nada. Haz
# por el momento el menú y que la opción de salir funcione
import os
import json

def add_contacto(nombre, telefono):
    dicti = {
        "nombre" : f"{nombre}",
        "telefono" : f"{telefono}"
    }
    return dicti


def encontrar_contacto(contacto):
    encontrado = False
    resultado = ""
    index_contact = 0
    for i in range(len(data)):
            if data[i]["nombre"] == contacto:
                encontrado = True
                index_contact = i
    if encontrado == True:
        resultado = f'{data[index_contact]["nombre"]} ---- {data[index_contact]["telefono"]}' 
    else:
        resultado = "No existe el contacto"
    return resultado

def index_contacto(contacto):
    if encontrar_contacto(contacto) == "No existe el contacto":
        return False
    else:
        for i in range(len(data)):
            if data[i]["nombre"] == contacto:
                index_contact = i
                return(index_contact)

bucle = 1
while bucle == 1:
    bucle_input= 1
    while bucle_input == 1:
        try:
            os.system("clear")
            print("1.   Dar de alta un contacto")
            print("2.   Buscar un contacto")
            print("3.   Eliminar un contacto")
            print("0.   Salir")
            print("")
            num = int(input("Escribe una opción = "))
            if num < 0 or num >3:
                print("")
                print("Tienes que escribir una opción")
            elif num == 0:
                os.system("clear")
                print("Adiós")
                print("Cerrando programa...")
                
                bucle_input = 0
                bucle = 0

            else:
                with open("agenda.json", "r") as agenda:
                    data = json.load(agenda)

                if num == 1:
                    os.system("clear")
                    print("------Dar de alta un contacto------")
                    nombre = input("Escribe el nombre = ")
                    telefono = input("Escribe el número = ")
                    data.append(add_contacto(nombre,telefono))
                    print("Usuario añadido correctamente")
                    print(nombre, " ---- ", telefono)
                    with open("agenda.json", "w") as agenda:
                        datos = json.dump(data, agenda, indent= 2)
                    print("\n \n \n")
                    salida = input("Pulsa Enter para salir al menú")
                elif num == 2:
                    os.system("clear")
                    print("------Buscar un contacto------")
                    print("")
                    contacto = input("Escribe el nombre de un contacto = ")
                    print(encontrar_contacto(contacto))

                    
                    print("\n \n \n")
                    salida = input("Pulsa Enter para salir al menú")
                elif num == 3:
                    os.system("clear")
                    print("------Eliminar un contacto------")
                    print("")
                    try:
                        contacto = input("Escribe el nombre del contacto = ")
                        if index_contacto(contacto) == False:
                            print("El contacto no existe")
                        else: 
                            data.pop(index_contacto(contacto))
                            with open("agenda.json", "w") as agenda:
                                datos = json.dump(data, agenda, indent= 2)
                            print("El contacto se ha borrado correctamente")
                        
                    except:
                        print("Error")
                    print("\n \n \n")
                    salida = input("Pulsa Enter para salir al menú ")
        except:
            print("Tienes que escribir una opción ")
