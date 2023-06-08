#Desafio: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
print('=+=+'*15)
print('Vamos verificar se há empréstimo disponível para você!')
print('_____ PREENCHA OS DADOS ABAIXO ____')
casa = float(input('Valor da casa: R$ '))
salario = float(input('Seu salário:R$ '))
anos = int(input('Quantos anos deseja pagar:'))
print('Calculando...')
parcela = casa/(anos*12)
if parcela <= salario*30/100: #essa é a forma correta de fazer porcentagem, a porcentagem divido por cem
    print(f'Você ira pagar R${parcela:.2f} por {anos} anos sem juros.')
else:
    print(f'Que pena, seu empréstimo não foi aprovado, saiba o porque: \n Pagando em {anos} meses, o valor da parcela fica em R${parcela} \n Isso corresponde a mais que 30% do seu salário que é R${salario}.')
