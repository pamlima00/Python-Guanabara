#DESAFIO: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: digita 6.127 e mostra inteiro 6.
from math import trunc

n = float(input('Me diga um número real:'))
i = trunc(n)
print(f'O número inteiro é: {n:.0f}')
print(f'O número inteito de {n} é {i}')