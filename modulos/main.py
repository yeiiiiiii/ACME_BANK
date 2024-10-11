import time
from Verificaciones import crear_cuenta
from Transacciones import *
from Extractos import mostrar_movimientos

banco = {
    "usuarios": [],
    "cuentas": [],
}

def menu():
    while True:
        print("\n              ACNE'S BANK                        \n")
        print("============== MENÚ DE OPCIONES ==================")
        print("============ 1. Crear cuenta=====================")
        print("============ 2. Consignar dinero=================")
        print("============ 3. Retirar dinero===================")
        print("============ 4. Pagar servicios==================")
        print("============ 5. Mostrar movimientos==============")
        print("============ 6. Salir============================")
        print("Escoge una opción:")
        opcion = int(input())

        print("Cargando...")
        time.sleep(2)
        if opcion == 1:
            crear_cuenta(banco)
        elif opcion == 2:
            consignar_dinero(banco)
        elif opcion == 3:
            retirar_dinero(banco)
        elif opcion == 4:
            pagar_servicio(banco)
        elif opcion == 5:
            mostrar_movimientos(banco)
        elif opcion == 6:
            print("Gracias por confiar en nosotros, bye <3")
            break
        else:
            print("Error, escoge las opciones que hay (1 al 6)")


menu()
