#DESAFIO: Crie um programa que leia o nome completo de uma pessoa e mostre:
    #o nome com todas as letras maiúsculas
    #o nome com todas as letras minúsculas
    #quantas letras ao todo (sem considerar os espaços)
    #quantas letras tem o primeiro nome

name = str(input('Qual seu nome completo?')).strip() #strip para separar espaços na frente ou no atrás que o usuário coloque
print('Analisando seu nome...')
print('Seu nome em maiúscilas é', name.upper())
print('Seu nome em minúscula é', name.lower())
print('Seu nome tem ao todo', len(name)-name.count(' '),'letras.') #faz-se uma operação para conta nome mas remover espaços
parte = name.split() #cria-se separação para contar o primeiro conjunto
print('Seu primeiro nome é', parte[0], len(parte[0]))