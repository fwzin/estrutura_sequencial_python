# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
# para homens: Peso = (72.7 * altura) – 58


print('')
print('calculadora do peso ideal')
print('')

Altura = float(input('digite sua altura: '))
print('')
Peso_Atual = float(input('digite seu peso atual: '))
print('')

S = (72.7 * Altura) - 58

print('')
print('Seu peso atual é de {}, mas de acordo com sua altura o seu peso ideal seria: {}'.format (Peso_Atual, S))