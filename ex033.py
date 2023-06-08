# DESAFIO: Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.
a = int(input('Diga um número: '))
b = int(input('Diga outro número: '))
c = int(input('Diga mais um outro número: '))
# para verificar qual é o menor, podemos dar um deles como o menor e criar if para mudar a regra se os demais forem maiores
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
# para verificar qual é o mair, é só repetir a lógica com novo nome de variável e sinal
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'Entre os números que você digitou, o maior é {maior}, e o menor é {menor}')
