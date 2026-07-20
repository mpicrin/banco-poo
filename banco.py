from ahorro import Ahorro
from corriente import Corriente

class Banco:
    def __init__(self):
        self.cuentas = []
        
    def agregar_cuenta(self):
        opc = int(input("1 - Cuenta corriente (prestamos y saldo negativo)\n2 - Cuenta Ahorro (2 % en ingresos > 2000)\n-> "))
        match opc:
            case 1:
                nombre = input("Nombre: ")
                titular = nombre.capitalize()
                self.cuentas.append(Corriente(titular,0))
                print("Cuenta Corriente creada. Saldo Inicial 0$")
            case 2:
                nombre = input("Nombre: ")
                titular = nombre.capitalize()
                self.cuentas.append(Ahorro(titular,0))
                print("Cuenta Ahorro creada. Saldo Inicial 0$")
            case _: print("No es opcion")
            
    def usar_cuenta(self):
        if not self.cuentas:
            "no hay Cuenta"
            return
        
        for i, c in enumerate(self.cuentas ,start=1):
            if isinstance(c, Corriente):
                print(f"{i} - C / {c.titular}")
            elif isinstance(c, Ahorro):
                print(f"{i} - A / {c.titular}")
        opc = int(input("-> ")) - 1
        return opc

    def rellenar_cuentas_prueba(self):
        self.cuentas = [
            Ahorro("Yhon",1000),
            Ahorro("Javier",500),
            Corriente("Ivan",10),
            Corriente("Hanna", 2000),
            Ahorro("Tom", 80),
            Corriente("Anna", 50000)]
            
def menu():
    print("""
    ___MENU__
    1. Crear Cuenta
    2. Usar Cuenta""")
    cc = input("-> ")
    b = Banco()
    usar = False 
    b.rellenar_cuentas_prueba()
    if cc == "1":
        b.agregar_cuenta()
    elif cc == "2":
        indice = b.usar_cuenta()
        usar = True
    else:
        print("Opcion desconocida")
        return
    
    while True:
        if not b.cuentas:
            print("No hay Cuentas...")
            break
        print('''
        ___MENU___
        1. Depositar
        2. Retirar
        3. Ver Estado
        
        _Para cuentas Corrientes_
        4. Pedir Prestamos
        5. Pagar Prestamos
        6. Ver Prestamos
        
        00. Reiniciar
        0. SALIR..''')
    
        opc = input("-> ")
        match opc:
            case "1":
                if usar:
                    b.cuentas[indice].depositar()
                else:
                    b.cuentas[-1].depositar()
            case "2":
                if usar:
                    b.cuentas[indice].retirar()
                else:
                    b.cuentas[-1].retirar()
            case "3":
                if usar:
                    b.cuentas[indice].ver_estado()
                else:
                    b.cuentas[-1].ver_estado()
            case "4":
                if usar:
                    if isinstance(b.cuentas[indice], Corriente):
                        b.cuentas[indice].agregar_prestamo()
                    else:
                        print("Su cuenta no es Corriente")
                else:
                    if isinstance(b.cuentas[-1], Corriente):
                        b.cuentas[-1].agregar_prestamo()
            case "5":
                if usar:
                    if isinstance(b.cuentas[indice], Corriente):
                        b.cuentas[indice].pagar_prestamo()
                    else:
                        print("Su cuenta no es Corriente")
                else:
                    if isinstance(b.cuentas[-1], Corriente):
                        b.cuentas[-1].pagar_prestamo()
            case "6":
                if usar:
                    if isinstance(b.cuentas[indice], Corriente):
                        b.cuentas[indice].ver_prestamo()
                    else:
                        print("Su cuenta no es Corriente")
                else:
                    if isinstance(b.cuentas[-1], Corriente):
                        b.cuentas[-1].ver_prestamo()
            case "00": menu()
            case "0": break
            case _: print("OPCION NO ENCONTRADA")
            
                
        
if __name__ == "__main__":
    menu()