#DESAFIO: Desenvolva um programa que leia as notas de um aluno, calcule e mostre sua média.
m = float(input('Nota de Matemática: '))
p = float(input('Nota de Português: '))
c = float(input('Nota de Ciências: '))
r = (m + p + c) / 3
print(f'Sua nota de Matemática é {m}, de Português é {p}, de Ciências é {c}. E sua média final é {r}.')