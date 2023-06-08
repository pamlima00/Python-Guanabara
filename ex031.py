#DESAFIO: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passage, cobrando R$0,50 por KM para viagens de até 200km e R$0,45 para viagens mais longas.
km = float(input('Quantos km é sua viagem: '))
if km <=200:
    print(f'Para sua viagem de {km}, o preço será de R$:', km*0.50)
else:
    print(f'Para sua viagem de {km}, o preço será de R$:', km*0.45)