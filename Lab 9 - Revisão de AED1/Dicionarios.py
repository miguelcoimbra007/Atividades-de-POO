
#Q1

def contagem_caracteres(texto):
    contagem = {}

    for caractere in texto:
        if caractere in contagem:
            contagem[caractere] = contagem[caractere] + 1
        else:
            contagem[caractere] = 1

    return contagem


frase = "Odeio Dicionario :( :"
resultado = contagem_caracteres(frase)
print(resultado)

#Q2

arquivo = open("estomago.txt")
texto = arquivo.read()
arquivo.close()

texto = texto.lower()
palavras = texto.split()

contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] = contagem[palavra] + 1
    else:
        contagem[palavra] = 1

ordenado = dict(sorted(contagem.items()))

print(ordenado)

# Pesquisinha leve rolou ne ;]

#Q3

def mesclar_dicionarios(d1, d2):
    resultado = {}

    for chave in d1:
        resultado[chave] = d1[chave]

    for chave in d2:
        if chave in resultado:
            if d2[chave] > resultado[chave]:
                resultado[chave] = d2[chave]
        else:
            resultado[chave] = d2[chave]

    return resultado

dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 4, 'd': 5}

resultado = mesclar_dicionarios(dicionario1, dicionario2)
print(resultado)

#Q4

def filtrar_dicionario(dados, chaves):
    resultado = {}

    for chave in chaves:
        if chave in dados:
            resultado[chave] = dados[chave]

    return resultado

dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
chaves_filtradas = ['a', 'c', 'e']

resultado = filtrar_dicionario(dados, chaves_filtradas)
print(resultado)

#Q5

def resultado_votacao(votos):
    total_por_candidato = {}
    total_geral = 0

    for sessao in votos:
        for candidato in sessao:
            if candidato in total_por_candidato:
                total_por_candidato[candidato] = total_por_candidato[candidato] + sessao[candidato]
            else:
                total_por_candidato[candidato] = sessao[candidato]

            total_geral = total_geral + sessao[candidato]

    resultado = {}

    for candidato in total_por_candidato:
        percentual = (total_por_candidato[candidato] / total_geral) * 100
        resultado[candidato] = (total_por_candidato[candidato], round(percentual, 2))

    return resultado

votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]

resultado = resultado_votacao(votos)
print(resultado)