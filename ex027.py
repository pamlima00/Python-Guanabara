#DESAFIO: Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o último nme separaramente.
nome =  str(input('Qual seu nome completo?')).strip().split()
print('Seu primeiro nome é', nome[0]) #o zero vai ler o primeiro valor
print('Seu último nome é', nome[-1]) #o negativo vai ler o último valor