from abc import ABC, abstractmethod

class Entrega(ABC):

    def __init__(self, endereco_destino, peso):
        self.endereco_destino = endereco_destino
        self.status = "Nada ainda"
        self.peso = peso

    def atualizar_status(self, status):
        self.status = status

    def imprimir_dados(self):
        print("endereco de destino:", self.endereco_destino)
        print("status:", self.status)
        print("Peso:", self.peso)

    def calcular_frete(self):
        pass


class EntregaTerrestre(Entrega):

    def __init__(self, endereco_destino, peso, distancia_km):
        super().__init__(endereco_destino, peso)
        self.distancia_km = distancia_km

    def imprimir_dados(self):
        super().imprimir_dados()
        print("istancia:", self.distancia_km, "km/hr")
        print("Frete:", self.calcular_frete(), "kwanzas")

    def calcular_frete(self):
        if self.distancia_km <= 100:
            return 20
        elif self.distancia_km <= 500:
            return 40 + 1.50 * self.peso
        else:
            return 70 + 2.20 * self.peso


class EntregaAerea(Entrega):

    def __init__(self, endereco_destino, peso, taxa_despacho):
        super().__init__(endereco_destino, peso)
        self.taxa_despacho = taxa_despacho

    def imprimir_dados(self):
        super().imprimir_dados()
        print("Taxa de despacho:", self.taxa_despacho, "reais")
        print("Frete:", self.calcular_frete(), "reais")

    def calcular_frete(self):
        return self.taxa_despacho + 12 * self.peso


entregas = []

while True:
    print()
    print("1 - Criar nova entrega")
    print("2 - Listar entregas")
    print("3 - Sair")
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        print()
        print("1 - Entrega terrestre")
        print("2 - Entrega aerea")
        tipo = input("Tipo de entrega: ")

        endereco = input("Endereco de destino: ")
        peso = float(input("Peso (kg): "))

        if tipo == "1":
            distancia = float(input("Distancia (km): "))
            entregas.append(EntregaTerrestre(endereco, peso, distancia))
            print("Entrega terrestre cadastrada!")

        elif tipo == "2":
            taxa = float(input("Taxa de despacho (reais): "))
            entregas.append(EntregaAerea(endereco, peso, taxa))
            print("Entrega aerea cadastrada!")

    elif opcao == "2":
        if len(entregas) == 0:
            print("Nenhuma entrega cadastrada.")
        else:
            for i in range(len(entregas)):
                print()
                print("Entrega", i + 1)
                entregas[i].imprimir_dados()

    elif opcao == "3":
        print("Encerrando o programa.")
        break