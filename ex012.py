#DESAFIO: Faça um algoritmo que leia o preço de um produto e mostre seus novo preço, com 5% de desconto.
preço = float(input('Qual é o preço do produto? R$'))
desc1 = (preço/100)*95
desc2 = preço-(preço*5/100)
print(f'Parabéns! Você ganhou 5% de desconto, o preço atual é R${desc1}')
print(f'Parabéns! Você ganhou 5% de desconto, o preço atual é R${desc2}')