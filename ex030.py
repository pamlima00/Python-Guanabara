#DESAFIO: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR
num = int(input('Me diga um número: '))
resul = num % 2 #fazer o '%' que é traz o número resto da divisão, sempre será 0 para números par e 1 para números impar
if resul == 0:
    print('Seu número é par!')
else:
    print('Seu número é ímpar!')
