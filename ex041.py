#Desafio: A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua caragotia, de acordo com a idade: até 9 anos MIRIM, até 14 anos INFANTIL; até 19 anos JUNIOR, até 20 anos SENIOR, acima MASTER
nasc = int(input('Qual seu ano de nascimento: '))
idade = 2023-nasc
if idade <9:
    print(f'Você é MIRIM. Você tem {idade} anos de idade.')
elif idade >10 and idade <14:
    print(f'Você é INFANTIL. Você tem {idade} anos de idade.')
elif idade >15 and idade <19:
    print(f'Você JUNIOR. Você tem {idade} anos de idade.')
elif idade == 20:
    print(f'Você é SÊNIOR. Você tem {idade} anos de idade.')
else:
    print(f'Você é MASTER. Você tem {idade} anos de idade.')