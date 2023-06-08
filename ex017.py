#Desafio: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um retângulo, calcule e mostre o comprimento da hipotenusa.
import math

co = float(input('Qual a medida do cateto oposto? '))
ca = float(input('Qual a medida do cateto adjacente? '))
qco = math.pow(co,2)
qca = math.pow(ca,2)
coca = qco + qca
hip = math.sqrt(coca)
hip2 = math.hypot(co,ca)
print(f'Se o cateto o posto é {co} e o cateto adjacente é {ca}, logo a hipotenusa é {hip:.2f} \n segundo resultado {hip2:.2f}')
