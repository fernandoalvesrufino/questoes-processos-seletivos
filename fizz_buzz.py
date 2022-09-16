# DESAFIO FIZZBUZZ - "Escreva um programa que imprima os números de 1 a 100. 
# Mas para múltiplos de três imprima 'Fizz' em vez do número e para os múltiplos de cinco imprima 'Buzz'. 
# Para números que são múltiplos de três e cinco imprimir 'FizzBuzz'".

for i in range(1, 101):                     # para cada 'valor' de 1 a 100, fazer
  if i % 3 == 0:                            # se o resto da divisao por 3 de 'valor' foi igual a 0
    if i % 5 == 0:                          # e se o resto da divisao por 5 de 'valor' foi igual a 0
      print('FIZZBUZZ', end = ' - ')        # imprimir "FIZZBUZZ"
    else:                                   # se o resto da divisao por 5 de 'valor' NÃO foi igual a 0, indica que apenas divisão por 3 é igual a 0
      print('Fizz', end = ' - ')            # imprimir "Fizz"
  elif i % 5 == 0:                          # se o resto da divisao apenas por 5 de 'valor' foi igual a 0
    print('Buzz', end = ' - ')              # imprimir "Buzz"
  else:                                     # senão
    print(i, end = ' - ')                   # imprime 'valor'
