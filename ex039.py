#Desafio: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: se ele ainda vai se alistar, se é a hora de se alistar, se já passou da hora de se alistar. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date #podemos usar ess módulo para chamar o ano atual
ano = int(input('Qual é o ano do seu nascimento: '))
idade = date.today().year-ano
if idade ==18:
    print('Você deve se alistar neste ano.')
elif idade <18:
    print(f'Ainda não está na hora de você se alistar. Faltam',18-idade,'anos.')
else:
    print(f'Você já deveria ter se alistado. Está atrasado em',idade-18,'anos.')