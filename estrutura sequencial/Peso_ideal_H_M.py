# tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

print('você é homem? ')

Sexo = int(input('S "1" ou N "2" :  '))
Altura = float(input('digite sua altura: '))

S1 = (72.7 * Altura) - 58
S2 = (62.1 * Altura) - 44.7

if Sexo > 1:
    print('seu peso ideal de acordo com sua altura é: {}'.format (S2))

else:
    print('seu peso ideal de acordo com sua altura é: {}'.format (S1))

