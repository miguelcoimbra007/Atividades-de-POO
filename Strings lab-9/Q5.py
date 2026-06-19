frase = input("Digite uma frase: ")
vogais = "aeiou"
indices = []

for i, letra in enumerate(frase):
    if letra.lower() in vogais:
        indices.append(i)

print(f"Total de vogais: {len(indices)}")
print(f"Índices das vogais: {indices}")