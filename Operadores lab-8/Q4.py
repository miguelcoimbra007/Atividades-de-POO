class Pessoa:

    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

    def __str__(self):
        return f"Nome: {self.nome} e Altura: {self.altura:.2f} centimetros."

    def __gt__(self, other):
        return self.altura > other.altura

    def __lt__(self, other):
        return self.altura < other.altura

psoa = []

quantidade = int(input("Quantas pessoas serã cadastradas? "))

for i in range(quantidade):
    nome = input("Nome: ")
    altura = float(input("Altura: "))

    pessoa = Pessoa(nome, altura)
    psoa.append(pessoa)

print("Pessoa mais alta:")
print(max(psoa))

print("Pessoa mais baixa:")
print(min(psoa))

print("Pessoas ordenadas por altura:")

for pessoa in sorted(psoa):
    print(pessoa)