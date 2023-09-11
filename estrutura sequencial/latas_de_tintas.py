"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
# serve para arrendondar para cima a quantidade de latas de tintas
import math

# Dados do produto
litros_por_metro_quadrado = 1 / 3
litros_por_lata = 18
preco_por_lata = 80.00

print('')
area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
print('')

quantidade_latas = math.ceil(area_a_ser_pintada / litros_por_metro_quadrado / litros_por_lata)
preco_total = quantidade_latas * preco_por_lata

print("Quantidade de latas de tinta a serem compradas:", quantidade_latas)
print("Preço total: R$", preco_total)
print('')
