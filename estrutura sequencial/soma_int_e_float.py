# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A) o produto do dobro do primeiro com metade do segundo .
# B) a soma do triplo do primeiro com o terceiro.
# C) o terceiro elevado ao cubo.

print('')
print('calculadora')
print('')
print('Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:')
print('A)  o produto do dobro do primeiro com metade do segundo.')
print('B) a soma do triplo do primeiro com o terceiro.')
print('C) o terceiro elevado ao cubo.')
print('')

N1 = int(input('digite um numero inteiro: '))
N2 = int(input('digite mais um numero inteiro: '))
N3 = float(input('digite um numero real: '))

S = N1 + N2 + N3
S1 = (N1 * N1) + (N2 / N2)
S2 = (N1 * N1 * N1) + N3
S3 = N3 * N3 * N3


print('')
print('a soma dos numeros {}, {} e {} é igual a {}'.format (N1, N2, N3, S))
print('')
print('o produto do dobro do primeiro "{}" com metade do segundo "{}" é igual a: {}'.format (N1, N2, S1))
print('')
print('a soma do triplo do primeiro "{}" com o terceiro "{}" e igual a: {}.'.format (N1, N3, S2))
print('')
print('o terceiro "{}" elevado ao cubo é igual a: {}'.format (N3, S3))