# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

F = float(input('Entre com a temperatura em graus Fahrenheit: '))

C = (F - 32) * (5 / 9)

print('Valor em Celsius: {0}°C'.format(C))