from cuenta import Cuenta

class Corriente(Cuenta):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)
        self.prestamos = []
    
    def agregar_prestamo(self):
        limite = 0
        for p in self.prestamos:
            limite += p["monto"]
        monto = int(input("Prestar: "))
        if limite + monto > 10000:
            print("Se exede del Limite de 10000$")
            return
        monto5 = monto + monto * 0.05
        self.saldo += monto
        prestamo = {"monto":monto, "pagar":monto5}
        self.prestamos.append(prestamo)
        
        
    def pagar_prestamo(self):
        if not self.prestamos:
            print("No Tiene Prestamos")
            return
        
        for i, p in enumerate(self.prestamos, start=1):
            print(f'{i} - Pedido: {p["monto"]}$  Pagar: {p["pagar"]}$')
        indice = int(input("-> ")) - 1
        
        print(f"Deuda: {self.prestamos[indice]["pagar"]}$ Saldo: {self.saldo}$")
        cant = int(input("Pagar: "))
        if cant - self.saldo < -5000:
            print(f'Limite de saldo negativo alcanzado (-5000$). Saldo actual {self.saldo}$')
            return
            
        if cant >= self.prestamos[indice]["pagar"]:
            self.saldo -= self.prestamos[indice]["pagar"]
            self.prestamos.pop(indice)
            print(f'Pago total de la deuda. Saldo restante {self.saldo}$')
        else:
            self.saldo -= cant
            self.prestamos[indice]["pagar"] -= cant
            print(f'Pago parcial de la deuda quedan {self.prestamos[indice]["pagar"]}$. Saldo restante {self.saldo}$')
        
            
    def ver_prestamo(self):
        if not self.prestamos:
            print("No Tiene Prestamos")
            return
        monto = 0
        pagar = 0
        for i, p in enumerate(self.prestamos, start=1):
            monto += p["monto"]
            pagar += p["pagar"]
            print(f'{i} - Pedido: {p["monto"]}$  Pagar: {p["pagar"]}$')
        print(f"__Monto Total: {monto}$ Total Pagar: {pagar}$__")
        
    def retirar(self):
        retiro = int(input("Retirar: "))
        if self.saldo - retiro < -5000:
            print(f'Limite de saldo negativo alcanzado (-5000$). Saldo actual {self.saldo}$')
        else:
            self.saldo -= retiro
            print(f'Se retiro {retiro}$ de su cuenta. Saldo actual {self.saldo}$')
        
    def ver_estado(self):
        if self.saldo >= 0:
            print(f"Cuenta Corriente\nTitular: {self.titular} Saldo: {self.saldo}$")
        else:
            print(f"Cuenta Corriente\nTitular: {self.titular} Saldo: {self.saldo}/-5000$")
            