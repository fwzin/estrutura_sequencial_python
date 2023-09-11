"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os 
valores para cima, isto é, considere latas cheias.
"""
#para arrendondar para cima os valores
import math

litros_por_metro_quadrado = 1 / 6
litros_por_lata = 18
preco_lata = 80.00
litros_por_galao = 3.6
preco_galao = 25.00
folga = 1.1  # 10% de folga

print('')
area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Calculo 18 litros
quantidade_latas = math.ceil((area_a_ser_pintada * litros_por_metro_quadrado * folga) / litros_por_lata)
preco_total_latas = quantidade_latas * preco_lata

# Calculo 3,6 litros
quantidade_galoes = math.ceil((area_a_ser_pintada * litros_por_metro_quadrado * folga) / litros_por_galao)
preco_total_galoes = quantidade_galoes * preco_galao

# Calculo da quantidade de tinta e preços para latas e galões combinados
quantidade_combinada_latas = quantidade_latas
quantidade_combinada_galoes = math.ceil((area_a_ser_pintada * litros_por_metro_quadrado * folga) / litros_por_galao) % math.ceil(litros_por_lata / litros_por_galao)
preco_total_combinado = (quantidade_combinada_latas * preco_lata) + (quantidade_combinada_galoes * preco_galao)


print("Situação 1: Comprar apenas latas de 18 litros")
print("Quantidade de latas de tinta a serem compradas:", quantidade_latas)
print("Preço total: R$", preco_total_latas)

print("\nSituação 2: Comprar apenas galões de 3,6 litros")
print("Quantidade de galões de tinta a serem comprados:", quantidade_galoes)
print("Preço total: R$", preco_total_galoes)

print("\nSituação 3: Misturar latas e galões")
print("Quantidade de latas de tinta a serem compradas:", quantidade_combinada_latas)
print("Quantidade de galões de tinta a serem comprados:", quantidade_combinada_galoes)
print("Preço total: R$", preco_total_combinado)
