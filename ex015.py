#DESAFIO: Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.
km = float(input('Quantos Km o carro percorreu?'))
dias = float(input('Por quantos dias ele foi alugado?'))
pkm = 0.15*km
pdias = 60*dias
print(f'O total a pagar é de R${pkm+pdias} \n Detalhado: \n O preço a pagar por {km}KM é de R${pkm}. \n E o preço a pagar {dias} é de R${pdias}.')