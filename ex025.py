#DESAFIO: Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome
nome = str(input('Qual seu nome completo?')).strip()
print('SILVA' in nome.upper()) #Classificado nome em upper para achar independente de estar maiusculo ou minusculo