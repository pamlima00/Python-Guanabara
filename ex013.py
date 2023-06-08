#DESAFIO: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual seu salário atual? R$'))
novo = salario+(salario*15/100)
print(f'Seu novo salário é R${novo}')