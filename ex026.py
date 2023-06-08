#DESAFIO:  Faça um programa que leia uma frase pelo teclado e mostre:
    #quantas vezes aparece a letra 'A'
    #em que popsição ela aparece a primeira vez
    #em que posição ela aparece a última vez

frase = str(input('Diga uma frase')).strip().upper()
print('Analisando sua frase percebemos que: ')
print('A letra "A" aparece: ', frase.count('A'))
print('A primeira posição da letra "A" é: ', frase.find('A')+1) #vai fazer a partir da primeira casa
print('A úlltima posição a letra "A" aparece é :', frase.rfind('A')+1) #vai fazer a busca do fim pro começo
