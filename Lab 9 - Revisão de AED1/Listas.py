# questão 01

numeros = []

print("Digite pelo menos 4 números inteiros.")
while True:
    numero = int(input("Número: "))
    numeros.append(numero)

    continuar = input("Deseja adicionar outro número? (s/n): ").lower()
    if continuar == "n" and len(numeros) >= 4:
        break

print("Lista:", numeros)
print("3 primeiros:", numeros[:3])
print("2 ultimos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Numeros Pares:", numeros[::2])
print("Numeros Impar:", numeros[1::2])


# questão 02

q = int(input("informe qnts urls"))
urls = []
urls2 = []

for i in range(0 , q):
        u = str(input("Mostra a url: "))
        urls.append(u)
        urls.append("www.{u}.com.br")

        print(urls)
        print(urls2)

# questão 03

from random import randint

lista = []

for i in range(10):
    lista.append(randint(-100, 100))

ordenada = sorted(lista)

print("ordenada:", ordenada)
print("original:", lista)
print("Índice do maior valor:", lista.index(max(lista)))
print("Índice do menor valor:", lista.index(min(lista)))
print("Soma:", sum(lista))
print("Media:", sum(lista) / len(lista))

#funções nativas

# questão 04



# questão 05

from random import randint

lista1 = []
lista2 = []

for i in range(20):
    lista1.append(randint(0, 50))
    lista2.append(randint(0, 50))

interseccao = sorted(list(set(lista1) & set(lista2)))

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Intersecção:", interseccao)


# questão 06

from random import randint

lista = []

for i in range(20):
    lista.append(randint(0, 100))

print("Lista original:")
print(lista)

tamanho = int(input("Tamanho para divisão: "))

sublistas = []

for i in range(0, len(lista), tamanho):
    sublistas.append(lista[i:i+tamanho])

print("Sublistas:")
print(sublistas)


# questão 07

n = int(input("Digite n: "))

matriz = []

for i in range(n):
    linha = []

    for j in range(n):
        linha.append(i)

    matriz.append(linha)

print("Resultado:")
for linha in matriz:
    print(linha)