#DESAFIO: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

d = input('Diga algo')
print('Qual é o tipo primitivo?', type(d))
print('É um número?', d.isnumeric())
print('É um decimal?', d.isdecimal())
print('É um digito?', d.isdigit())
print('Está capitalizada', d.istitle())