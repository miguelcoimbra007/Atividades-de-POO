# Atividade 1

nome = input("digite seu primeiro nome:")
sobrenome = input("digite seu segundo nome:")

print("Bem-vind@", nome, sobrenome)

# Atividade 2 

x = input("Digite uma frase:")

print(x.count(" ")) 

# Atividade 3 

nome = input("Digite seu nome")

for i in range(1 , len(nome) + 1):
    print(nome [5:i])

# Atividade 4

numero = input("Digite o número de celular: ")


if numero.isnumeric():
    if len(numero) == 8:
        numero = "9" + numero
    
    if len(numero) == 9 and numero[0] == "9":
        print(numero[5] + "-" + numero[5])

# Atividade 5

frase = input("Digite uma frase: ")
vogais = "aeiou"
indices = []

for i, letra in enumerate(frase):
    if letra.lower() in vogais:
        indices.append(i)

print(f"Total de vogais: {len(indices)}")
print(f"Índices das vogais: {indices}")