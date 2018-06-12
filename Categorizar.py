#!/usr/bin/env python3
##############################################################
# Programa desarrollado por @fotosycaptura                   #
# Informar bugs o sugerencias                                #
# Requiere Python 3.x para su funcionamiento                 #
##############################################################

import filecmp, shutil, os
from os import scandir, getcwd
from os.path import abspath
from os.path import join, getsize
from os.path import isfile

#---------------- ls ----------------------#
"""
Define un ls para obtener un listado de archivos
"""
def ls(ruta = getcwd()):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]

"""
Crea la carpeta segun el modelo de cámara que se le asigne
"""
def crearModelo(strCam, strModel):
    print('Procesando...')
    carpetas = os.listdir(getcwd())
    for carp in carpetas:
        #controlar error al no ser carpeta
        """ Se verifica si no es archivo, es decir, que sea carpeta """
        if (not isfile(carp)):
            """
            Se debería tambien de validar si es necesario crear la carpeta
            En caso de no existir archivos creo que no sería necesario llevar
            esto a cabo
            """
            hayArchivos = ls(carp)
            if (len(hayArchivos) > 0):
                if not os.path.exists(carp + os.sep + strCam + strModel):
                    os.makedirs(carp + os.sep + strCam + strModel)
                #for carp in carpetas:
                archivos = ls(carp)
                for i in archivos:
                        shutil.move(i, carp + os.sep + strCam + strModel)
        print('.')


def menu():
    
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    os.system('cls') # NOTA para windows tienes que cambiar clear por cls
    print ("Selecciona una opción")
    print ("\t 1 - Canon/550D")
    print ("\t 2 - Canon/EOSM")
    print ("\t 3 - Canon/PSELPH-320HS")
    print ("\t 4 - SonyEricson/W800i")
    print ("\t 5 - SonyEricson/W995")
    print ("\t 6 - SonyEricson/U20a")
    print ("\t 7 - Nikon/CoolpixL100")
    print ("\t 8 - Dlink")
    print ("\t 9 - Samsung/GT-S5830L")
    print ("\t10 - Samsung/PL210")
    print ("\t11 - Asus/Tablet")
    print ("\t12 - HTC/OneX")
    print ("\t13 - Moto/X")
    print ("\t99 - salir")

def run():
    while True:
        menu()
        # solicituamos una opción al usuario
        opcionMenu = input("inserta un numero valor >> ")
        if opcionMenu=="1":
                print ("")
                input("Has pulsado la opción 1...\npulsa una tecla para continuar")
                crearModelo('CN', '550D')
        elif opcionMenu=="2":
                print ("")
                input("Has pulsado la opción 2...\npulsa una tecla para continuar")
                crearModelo('CN', 'EOSM')
        elif opcionMenu=="3":
                print ("")
                input("Has pulsado la opción 3...\npulsa una tecla para continuar")
                crearModelo('CN', 'PSELPH-320HS')
        elif opcionMenu=="4":
                print ("")
                input("Has pulsado la opción 4...\npulsa una tecla para continuar")
                crearModelo('SE', 'W800i')
        elif opcionMenu=="5":
                print ("")
                input("Has pulsado la opción 5...\npulsa una tecla para continuar")
                crearModelo('SE', 'W995')
        elif opcionMenu=="6":
                print ("")
                input("Has pulsado la opción 6...\npulsa una tecla para continuar")
                crearModelo('SE', 'U20a')
        elif opcionMenu=="7":
                print ("")
                input("Has pulsado la opción 7...\npulsa una tecla para continuar")
                crearModelo('NK', 'CoolPixL100')
        elif opcionMenu=="8":
                print ("")
                input("Has pulsado la opción 8...\npulsa una tecla para continuar")
                crearModelo('DLink', '')
        elif opcionMenu=="9":
                print ("")
                input("Has pulsado la opción 9...\npulsa una tecla para continuar")
                crearModelo('Ssn', 'GT-S5830L')
        elif opcionMenu=="10":
                print ("")
                input("Has pulsado la opción 10...\npulsa una tecla para continuar")
                crearModelo('Ssn', 'PL210')
        elif opcionMenu=="11":
                print ("")
                input("Has pulsado la opción 11...\npulsa una tecla para continuar")
                crearModelo('Asus', 'Tablet')
        elif opcionMenu=="12":
                print ("")
                input("Has pulsado la opción 12...\npulsa una tecla para continuar")
                crearModelo('Htc', 'OneX')
        elif opcionMenu=="13":
                print ("")
                input("Has pulsado la opción 13...\npulsa una tecla para continuar")
                crearModelo('Moto', 'X')
        elif opcionMenu=="99":
                break
        else:
                print ("")
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

   
if __name__ == '__main__':
        run()
