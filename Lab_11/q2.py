from abc import ABC, abstractmethod


class MeioPagamento(ABC):

    def __init__(self):
        self.status = "pendente"

   
    def processar(self):
        pass
    
    def cancelar(self):
        pass

    def comprovante(self):
        pass

class CartaoCredito(MeioPagamento):

    def __init__(self, numero):
        super().__init__()
        self.numero = numero

    def processar(self):
        self.status = "aprovado"
        print("Pagamento no cartão aprovado!")

    def cancelar(self):
        self.status = "cancelado"
        print("Pagamento no cartão cancelado.")

    def comprovante(self):
        if self.status == "aprovado":
            print(f"Comprovante cartão final: {self.numero[-4:]}")
        elif self.status == "cancelado":
            print("Pagamento cancelado.")
        else:
            print("Pagamento pendente.")



class Pix(MeioPagamento):

    def __init__(self, chave):
        super().__init__()
        self.chave = chave

    def processar(self):
        self.status = "aprovado"
        print(f"Pix gerado para a chave: {self.chave}")

    def cancelar(self):
        print("Pix não pode ser cancelado.")

    def comprovante(self):
        if self.status == "aprovado":
            print("Comprovante Pix gerado!")
        else:
            print("Pix não pago.")



class Boleto(MeioPagamento):

    def __init__(self, codigo):
        super().__init__()
        self.codigo = codigo

    def processar(self):
        self.status = "aprovado"
        print(f"Boleto gerado: {self.codigo}")

    def cancelar(self):
        self.status = "cancelado"
        print("Boleto cancelado.")

    def comprovante(self):
        if self.status == "aprovado":
            print("Comprovante do Boleto gerado!")
        elif self.status == "cancelado":
            print("Boleto cancelado.")
        else:
            print("Boleto pendente.")

print("1-Cartão | 2-Pix | 3-Boleto")
opcao = input("Opção: ")

if opcao == "1":
    pagamento = CartaoCredito(input("Número do Cartão: "))
elif opcao == "2":
    pagamento = Pix(input("Chave Pix: "))
elif opcao == "3":
    pagamento = Boleto(input("Código de Barras: "))

pagamento.processar()
pagamento.comprovante()