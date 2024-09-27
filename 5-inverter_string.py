def inverter(string):
    #return string[::-1]

    # convertendo a string em uma lista, pois as strings sao imutaveis
    string = list(string)
    tam = len(string)//2

    # inverte os caracteres iniciando pelo primeiro e ultimo, depois segundo e penultimo sucessivamente
    for i in range(tam):
        string[i], string[len(string)-1-i] = string[len(string)-1-i], string[i]
    
    # retorna a lista convertida em string
    return "".join(string)

if __name__ == "__main__":
    # string definida pelo usuario
    string = input("Digite uma string: ")
    print(inverter(string))