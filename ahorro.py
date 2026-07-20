from cuenta import Cuenta

class Ahorro(Cuenta):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)
        
    def ver_estado(self):
        print(f"Cuenta Ahorro\nTitular: {self.titular} Saldo: {self.saldo}$")
    
    def depositar(self):
        ingreso = int(input("Ingresar: "))
        if ingreso > 2000:
            ingreso *= 0.02
        self.saldo += ingreso
        print(f'Se ingreso {ingreso}$ a su cuenta. Saldo actual {self.saldo}$')
    