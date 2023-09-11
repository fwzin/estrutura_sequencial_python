# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

N1 = int(input('digite a primeira nota: '))
N2 = int(input('digite a segunda nota: '))
N3 = int(input('digite a terceiro nota: '))
N4 = int(input('digite a quarto nota: '))

media = N1 + N2 + N3 + N4
media2 = media / 4

print('a media das notas', N1, N2, N3, 'e', N4, 'e igual a:', media2)