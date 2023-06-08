#DESAFIO: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.2500,00, calcile um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Qual seu salário: '))
if sal >= 1250:
    print('Seu salário vai aumentar para: R$', (10 * sal) / 100 + sal)
else:
    print('Seu salário vai aumentar para: R$', (15 * sal) / 100 + sal)
