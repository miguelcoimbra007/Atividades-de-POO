numero = input("Digite o número de celular: ")


if numero.isnumeric():
    if len(numero) == 8:
        numero = "9" + numero
    
    if len(numero) == 9 and numero[0] == "9":
        print(numero[5] + "-" + numero[5])
