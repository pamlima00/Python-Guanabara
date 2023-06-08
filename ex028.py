#DESAFIO: Escreva um programa que faça o computador 'pensar' em um número inteiro antes de 0 e 5, e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
from time import sleep #o sleep faz um delay para mandar o próximo comando
computador = randint(0, 5) #comando randomiza entre esses números
print('-=-'*20) #print pra deixar mais bonito
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-'*20) #print pra deixar mais bonito
jogadoor = int(input('Em qual número eu pensei? '))
print('Processando...')
sleep(2) #aciona o comando sleep
if  jogadoor == computador:
    print('PARABÉNS!! Você acertou miserávii')
else:
    print(f'POXA VIDA VOCÊ É BURRÃO EMM. Eu pensei no número {computador} e não no {jogadoor}')
