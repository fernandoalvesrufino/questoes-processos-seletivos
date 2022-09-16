def contar_caracteres(s):  # Criada a funcao contar_caracteres
    ''' Função que conta os caracteres de uma string

    Ex:
    >>> contar_caracteres('fernando')
    {'a': 1, 'd': 1, 'e': 1, 'f': 1, 'n': 2, 'o': 1, 'r': 1}

    :param s: string a ser contada

    '''

    resultado = {}

    for caracter in s:  # Para cada caracter da string em s
        resultado[caracter] = resultado.get(caracter,
                                            0) + 1  # Verifica se esse caracter está no dicionário resultado, se não estiver adiciona 1

    return resultado


if __name__ == '__main__':
    # Usado para controlar o escopo de execução, ou seja, o código não vai executar se estiver sendo apenas importado
    print(contar_caracteres('fernando'))  # Chama a função e envia o parametro 'fernando'
    print()  # pula linha
    print(contar_caracteres('gabriella'))  # Chama a função e envia o parametro 'gabriella'