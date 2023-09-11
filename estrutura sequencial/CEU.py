# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.


C = float(input('Entre com a temperatura em graus Celsius: '))

F = C * (9 / 5) + 32

print('Valor em Fahrenheit: {0}°F'.format(F))