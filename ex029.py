#DESAFIO: Escreva um programa que leia a velocodade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.
km = float(input('Em qual velocidade você estava?'))
if km <=79:
    print('Você está dentro do limite de velocidade')
else: print(f'MULTA NA CERTA!! \n Você estava há {km}km/h. \n Você deve pagar:R$', (km-80)*7)
print('\n Se liga, dirige direito caraio')