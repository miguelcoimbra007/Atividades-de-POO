lista = [10, 20, 30, 40, 50]

indice = int(input("Digite um indici: "))

try:
    print(lista[indice])
except IndexError:
    print("esse indice não existe na lista.")