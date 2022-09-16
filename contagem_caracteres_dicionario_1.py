def contar_caracteres(s):  # Criada a funcao contar_caracteres
    ''' Função que conta os caracteres de uma string

    Ex:
    >>> contar_caracteres('fernando')
    {'a': 1, 'd': 1, 'e': 1, 'f': 1, 'n': 2, 'o': 1, 'r': 1}

    :param s: string a ser contada

    '''

    caracteres_ordenados = sorted(s)  # Ordenados os caracteres

    caracter_anterior = caracteres_ordenados[0]  # Utiliza o caracter anterior como referencia
    contagem = 1  # Inicia a contagem

    resultado = {}

    for caracter in caracteres_ordenados[1:]:  # Para cada caracter da string analisada (a partir do segundo caracter)
        if caracter == caracter_anterior:  # se o caractere for igual ao caracter anterior
            contagem += 1  # adiciona mais um à contagem
        else:  # senão
            resultado[
                caracter_anterior] = contagem  # adiciona ao dicionario o caracter analisado e a qtde de vezes que ele é apresentado
            caracter_anterior = caracter  # define o ultimo caracter verificado como caracter_anterior para continuar testes
            contagem = 1  # Reinicia a contagem para 1

    resultado[caracter_anterior] = contagem  # adiciona ao dicionario o ultimo caracter verificado e sua contagem

    return resultado


if __name__ == '__main__':
    # Usado para controlar o escopo de execução, ou seja, o código não vai executar se estiver sendo apenas importado
    print(contar_caracteres('fernando'))  # Chama a função e envia o parametro 'fernando'
    print()  # pula linha
    print(contar_caracteres('gabriella'))  # Chama a função e envia o parametro 'gabriella'
