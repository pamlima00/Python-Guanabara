#DESAFIO: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Que ano quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #pela regra do bissexto ele tem que ser divisivel por 4, porém não vale pra multiplos de 100 e nem multiplos de 400
    print(f'Você disse o ano {ano} Esse ano é bissexto!')
else:
    print(f'Você disse o ano {ano}. \n ELE NÃO É BISSEXXXXX!!!')
