#DESAFIO: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos: ex: 19834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1
number = str(input('Me diga um número')).strip()
print('Analisando seu número... \n ______________________')
print('Sua unidade é:', (number[3]))
print('Sua dezena é:', (number[2]))
print('Sua centena é:', (number[1]))
print('Seu milhar é:', (number[0]))