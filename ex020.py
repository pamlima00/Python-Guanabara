#Desafio: O professor que sortear a ordem de apresentação de um trabalho de quatro alunos
import random
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista) #já foi relatada a lista, a sequência é dar um shuffle na lista e mostrar na print
print (f'O escolhido é : {lista}')