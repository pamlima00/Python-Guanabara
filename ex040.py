#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma menssagem no final, de acordo com a média atingida: média abaixo de 5.0 reprovado, média entre 5.0 e 6;0 recuperação, média 7.0 aprovado.
mat = float(input('Nota em Matemática: '))
por = float(input('Nota em Português: '))
cie = float(input('Nota em Ciências: '))
media = (mat + por + cie)/3
if media <5:
    print(f'\033[1;31; m REPROVADO \n Sua média é {media:.2f}.')
elif media >5.1 and media <6.9:
    print(f'\033[1;33; m EM RECUPERAÇÃO \n Sua média é {media:.2f}, estude mais.')
else:
    print(f'\033[7;32; m APROVADO \n Sua média é {media:.2f}.')
