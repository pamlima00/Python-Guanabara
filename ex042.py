#Desafio: Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: Equilátero: todos os lados iguais, Isósceles: dois lados iguais, Escaleno: todos os lados diferentes.
reta1 = float(input('\033[1;35;40m Qual tamanho da reta 1: ')) #usamos o padrão ANSI para dar cor utilizando o padrão \033[__;__;__m
reta2 = float(input('\033[1;35;40m Qual tamanho da reta 2: '))
reta3 = float(input('\033[1;35;40m Qual tamanho da reta 3:\033[m')) #para a cor ir até onde os caracteres vão, é só colocar no fim o código \033[m
#na regra matemática, para se ter um triangulo, cada uma das retas tem que ser menor do que a soma do comprimento dos outros dois
if reta1 < reta2 + reta3 and reta2 < reta3 + reta1 and reta3 < reta1 + reta2:
    print('Opa! Da pra montar um triangulo emm.')
elif reta1 == reta2 and reta3 == reta2:
    print('Este triângulo será um Equilátero com todos os lados iguais.')
else:
    print('Que pena, não é um triangulo :(')