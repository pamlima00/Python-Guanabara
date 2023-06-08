#Desafio: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
an = float(input('Qual é o valor do ângulo?')) #como o ângulo é medido em graus, foi colocado math.radians para calcular
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print(f'Para o ângulo de {an}º temos: \n Seno: {seno:.2f} \n Cosseno: {cosseno:.2f} \n Tangente: {tangente:.2f}')