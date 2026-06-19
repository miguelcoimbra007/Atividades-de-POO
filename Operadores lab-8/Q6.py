import random


class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def tomar_dano(self, valor):
        self.vida -= valor


class Mago(Personagem):
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida)
        self.mana = mana

    def __str__(self):
        return f"Nome: {self.nome} | Vida: {self.vida} | Mana: {self.mana:.2f}"

    def __add__(self, valor):
        self.mana += valor
        return self.mana

    def __sub__(self, valor):
        self.mana -= valor
        if self.mana < 0:
            self.mana = 0
        return self.mana

    def __mul__(self, fator):
        self.mana *= fator
        return self.mana

    def __truediv__(self, valor):
        self.mana /= valor
        return self.mana


class Barbaro(Personagem):
    def __init__(self, nome, vida, stamina):
        super().__init__(nome, vida)
        self.furia = False
        self.stamina = stamina

    def __str__(self):
        return f"Nome: {self.nome} | Vida: {self.vida} | Fúria: {self.furia} | Stamina: {self.stamina:.2f}"

    def __add__(self, valor):
        if self.furia:
            self.stamina += valor * 1.5
        else:
            self.stamina += valor
        return self.stamina

    def __sub__(self, valor):
        self.stamina -= valor

        if self.stamina <= 0 and not self.furia:
            self.furia = True
            self.stamina = 5

        return self.stamina

    def __mul__(self, fator):
        self.stamina *= fator
        if self.furia:
            self.vida += 5
        return self.stamina

    def __truediv__(self, valor):
        self.stamina /= valor
        return self.stamina


tipo = input("Escolha o tipo (Mago ou Barbaro): ").lower()
nome = input("Nome do personagem: ")
vida = int(input("Vida: "))

if tipo == "mago":
    mana = float(input("Mana: "))
    personagem = Mago(nome, vida, mana)

elif tipo == "barbaro":
    stamina = float(input("Stamina: "))
    personagem = Barbaro(nome, vida, stamina)

else:
    print("Tipo inválido")
    exit()


while True:

    print("======================")
    print(personagem)
    print("======================")
    print("1 - Tomar poção simples (+)")
    print("2 - Tomar poção especial (*)")
    print("3 - Ataque básico (-)")
    print("4 - Ataque especial (/)")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "0":
        break

    if isinstance(personagem, Mago):

        if op == "1":
            personagem + 5
        elif op == "2":
            personagem * 1.5
        elif op == "3":
            personagem - 2
        elif op == "4":
            personagem / 2

    elif isinstance(personagem, Barbaro):

        if op == "1":
            personagem + 5
        elif op == "2":
            personagem * 1.5
        elif op == "3":
            personagem - 2
        elif op == "4":
            personagem / 2

    dano = random.randint(1, 10)
    personagem.tomar_dano(dano)

    print(f"Você tomou {dano} de dano")
    print(f"Vida atual: {personagem.vida}")

    if personagem.vida <= 0:
        print("Você morreu")
        break