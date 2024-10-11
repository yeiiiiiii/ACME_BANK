from datetime import datetime
from Verificaciones import autenticar_usuario

def consignar_dinero(banco):
    print("\n------------------------------------------")
    print("---------CONSIGANACIÓN DE DINERO----------")
    print("------------------------------------------")
    usuario = autenticar_usuario(banco)
    if usuario:
        for cuenta in banco["cuentas"]:
            if cuenta["codigo_cuenta"] == usuario["codigo_cuenta"]:
                print("Ingrese el monto que va a consignar:")
                monto = int(input())
                cuenta["saldo"] += monto
                print("--------------------------------------------------")
                cuenta["movimientos"].append(f"Fecha: {datetime.now()} Tipo de movimiento: Entrada de dinero. Detalle: Consignación a su cuenta: ${monto}")
                print(f"Consignación exitosa, su saldo actual es de: ${cuenta['saldo']}")
                return 

def retirar_dinero(banco):
    print("\n--------------------------------")
    print("-------------RETIRO-------------")
    print("--------------------------------")
    usuario = autenticar_usuario(banco)
    if usuario:
        for cuenta in banco["cuentas"]:
            if cuenta["codigo_cuenta"] == usuario["codigo_cuenta"]:
                print("Ingrese el monto que va a retirar:")
                monto = int(input())
                if monto <= cuenta["saldo"]:
                    cuenta["saldo"] -= monto
                    print("----------------------------------------------------------")
                    cuenta["movimientos"].append(f"Fecha: {datetime.now()}. Tipo de movimiento: Salida de dinero. Detalle: Retiró: ${monto}")
                    print(f"Retiro exitoso, su nuevo saldo es de: ${cuenta['saldo']}")
                else:
                    print("Saldo insuficiente no puede realizar el retiro")
                return

def pagar_servicio(banco):
    print("\n---------------------------------------")
    print("-----------PAGO DE SERVICIOS-----------")
    print("---------------------------------------")
    usuario = autenticar_usuario(banco)
    if usuario:
        for cuenta in banco["cuentas"]:
            if cuenta["codigo_cuenta"] == usuario["codigo_cuenta"]:
                print("Seleccione el servicio a pagar")
                print("--------------------------------------------------")
                print("1. Energía \n2. Agua  \n3. Gas")
                print("Escoge una opción:")
                opcion = int(input())
                print("--------------------------------------------------")
                print("Referencia del servicio:")
                referencia = input()
                print("Ingrese el monto a pagar:")
                monto = int(input())
                if opcion ==1:
                    if monto <= cuenta["saldo"]:
                        cuenta["saldo"] -= monto
                        cuenta["movimientos"].append(f"Fecha: {datetime.now()}. Tipo de movimiento: Salida de dinero. Detalle: Pago del servicio de energía  con referencia: {referencia} por valor de ${monto}")
                        print("------------------------------------------------")
                        print(f"Pago de la factura de energia exitoso, su saldo disponible es: ${cuenta['saldo']}")
                    else:
                        print("Saldo insuficiente para realizar el pago")
                elif opcion ==2:
                    if monto <= cuenta["saldo"]:
                        cuenta["saldo"] -= monto
                        cuenta["movimientos"].append(f"Fecha: {datetime.now()}. Tipo de movimiento: Salida de dinero. Detalle: Pago del servicio de agua con referencia: {referencia} por valor de ${monto}")
                        print("------------------------------------------------")
                        print(f"Pago del servicio del agua exitoso, su saldo disponible es: ${cuenta['saldo']}")
                    else:
                        print("Saldo insuficiente para realizar el pago")
                elif opcion ==3:
                    if monto <= cuenta["saldo"]:
                        cuenta["saldo"] -= monto
                        cuenta["movimientos"].append(f"Fecha: {datetime.now()}. Tipo de movimiento: Salida de dinero. Detalle: Pago del servicio del gas con referencia: {referencia} por valor de ${monto}")
                        print("------------------------------------------------")
                        print(f"Pago del servicio del gas exitoso, su saldo disponible es: ${cuenta['saldo']}")  
                    else:
                        print("Saldo insuficiente para realizar el pago")  
                else:
                    print("Opción no valida")
                return