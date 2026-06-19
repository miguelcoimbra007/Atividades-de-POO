class Carteira:
    def __init__(self, moeda, saldo):
        self.moeda = moeda
        self.saldo = saldo

    def __add__(self, valor_yuan):
        if self.moeda == "USD":
            valor_convertido = valor_yuan * 0.14

        elif self.moeda == "BRL":
            valor_convertido = valor_yuan * 0.85

        else:  
            valor_convertido = valor_yuan

        return self.saldo + valor_convertido

    def __sub__(self, valor_yuan):
        if self.moeda == "USD":
            valor_convertido = valor_yuan * 0.14

        elif self.moeda == "BRL":
            valor_convertido = valor_yuan * 0.85

        else:  
            valor_convertido = valor_yuan

        return self.saldo - valor_convertido


carteira_usd = Carteira("USD", 10.0)

print("Soma de carteira USD + 50 yuan =", carteira_usd + 50.0)
print("Subtração de carteira USD - 50 yuan =", carteira_usd - 50.0)