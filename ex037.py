#Desafio: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversãp: 1 para binário, 2 para octal, 3 para hexadedecimal
n = int(input('Me diga um número: '))
q = int(input('Para qual base de conversão deseja aplicar: \n 1 - Binário \n 2 - Octal \n 3 - Hexadecimal \n Sua escolha: '))
if q == 1:
    print(f'A conversão em Binário é: {bin(n)[2:]}')
elif q == 2:
    print(f'A conversão em Octal é: {oct(n)[2:]}')
elif q == 3:
    print(f'A conversão em Hexadecimal é: {hex(n)[2:]}')
else:
    print('O número que você digitou não é uma opção válida.')