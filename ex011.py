#DESAFIO: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-lá, sabendo que cada litro de tinta pinta uma área de 2m².
largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura*altura
tinta = area/2
print(f'Para uma parede de {area:.2f}m², precisa de {tinta:.2f} litros de tinta.')
