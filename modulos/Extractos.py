from Verificaciones import autenticar_usuario

def mostrar_movimientos(banco):
    usuario = autenticar_usuario(banco)
    if usuario:
        for cuenta in banco["cuentas"]:
            if cuenta["codigo_cuenta"] == usuario["codigo_cuenta"]:
                print("\n----------------------------------------------------")
                print("----------------------MOVIMIENTOS-------------------")
                print("----------------------------------------------------")
                for movimiento in cuenta["movimientos"]:
                    print(movimiento)
                return