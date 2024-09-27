import json
import numpy as np

def menorFaturamento(dados):
    menor = np.inf
    for i in range(0, len(dados)):
        if dados[i]['valor'] < menor and dados[i]['valor'] != 0:
            menor = dados[i]['valor']
    return menor

def maiorFaturamento(dados):
    maior = dados[0]['valor']
    for i in range(1, len(dados)):
        if dados[i]['valor'] > maior:
            maior = dados[i]['valor']
    return maior

def mediaFaturamento(dados):
    soma = 0
    for i in range(len(dados)):
        if dados[i]['valor'] != 0:
            soma += dados[i]['valor']
    return soma/len(dados)

def diasAcimaMedia(dados):
    media = mediaFaturamento(dados)
    dias = 0
    for i in range(len(dados)):
        if dados[i]['valor'] > media:
            dias += 1
    return dias

if __name__ == "__main__":
    with open('dados.json', 'r') as arquivo:
        dados = json.load(arquivo)

    print("Menor faturamento: R$ %.2f" % menorFaturamento(dados))
    print("Maior faturamento: R$ %.2f" % maiorFaturamento(dados))
    print("Media de faturamento: R$ %.2f" % mediaFaturamento(dados))
    print("Dias com faturamento acima da media: %d" % diasAcimaMedia(dados))