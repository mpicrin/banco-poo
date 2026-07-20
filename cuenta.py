class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self):
        ingreso = int(input("Ingresar: "))
        self.saldo += ingreso
        print(f'Se ingreso {ingreso}$ a su cuenta. Saldo actual {self.saldo}$')
        
    def retirar(self):
        retiro = int(input("Retirar: "))
        if retiro < self.saldo:
            self.saldo -= retiro
            print(f'Se retiro {retiro}$ de su cuenta. Saldo actual {self.saldo}$')
        else:
            print(f'No dispone de esa cantidad ({self.saldo}$)')
    
    def ver_estado(self):
        pass