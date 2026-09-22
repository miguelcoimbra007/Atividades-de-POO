def verificar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa.")
    if idade < 18:
        raise ValueError("Idade mínima para tirar carteira é 18 anos.")
    print("Idade válida para tirar carteira.")

for idade in [-5, 15, 20]:
    try:
        verificar_idade(idade)
    except ValueError as erro:
        print(erro)