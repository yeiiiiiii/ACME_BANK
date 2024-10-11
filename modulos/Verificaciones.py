from datetime import datetime
def crear_cuenta(banco):
    print("\nIngrese su número de documento: ")
    documento = input()
    print("Ingrese su nombre: ")
    nombre = input()
    print("Ingrese clave: ")
    clave = input()
    print('Ingrese su clave de nuevo: ')
    clave2 = input()

    for usuario in banco["usuarios"]:
        if usuario["documento"] == documento:
            print("Usuario ya registrado.")
            return

    if clave == clave2:
        print("Clave asignada")
        codigo_cuenta = len(banco["cuentas"]) + 1

        nuevo_usuario = {
            "nombre": nombre, 
            "documento": documento, 
            "clave": clave, 
            "codigo_cuenta": codigo_cuenta
        }
        nueva_cuenta = {
            "codigo_cuenta": codigo_cuenta, 
            "documento": documento, 
            "saldo": 0, 
            "movimientos": []
        }
        
        banco["cuentas"].append(nueva_cuenta)
        banco["usuarios"].append(nuevo_usuario)
        
        print("------------------------------------------------------------------------")
        print(f"---ACNE'S BANK--- le da la bienvenida {nombre}")
        print(f"Registro exitoso.\nSu documento de identidad es: {documento}.\nSu número de cuenta es: {codigo_cuenta}.\nSu saldo actual es: {nueva_cuenta['saldo']}.\nFecha de creación: {datetime.now()}")
        print("------------------------------------------------------------------------")
    else:
        print("La contraseña no es la misma.")
        print("------------------------------------------------------------------------")
def autenticar_usuario(banco):
    print("Escoge una opción para iniciar tu cuenta:")
    print("1. Código de cuenta\n2. Número de documento")
    print("Escoge la opción:")
    opcion = int(input())
    if opcion == 1:
        print("Ingrese su código de cuenta: ")
        codigo_cuenta = int(input())
        print("Ingrese su clave: ")
        clave = input()
        for usuario in banco["usuarios"]:
            if usuario["codigo_cuenta"] == codigo_cuenta and usuario["clave"] == clave:
                return usuario
    elif opcion == 2:
        print("Ingrese su número de documento: ")
        documento = input()
        print("Ingrese su clave: ")
        clave = input()
        for usuario in banco["usuarios"]:
            if usuario["documento"] == documento and usuario["clave"] == clave:
                return usuario
    print("Autenticación fallida.")
    return None