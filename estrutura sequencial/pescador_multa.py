# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) 
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João 
# deverá pagar. Imprima os dados do programa com as mensagens adequadas.

print('')
print('calculadora da multa sobre o peso do peixe')
print('')

especie = str(input('qual é a especie do peixe: '))
Peixe = float(input('qual é o peso do peixe: '))
print('')
print('')

if  Peixe > 50:
    multa = (Peixe - 50) * 4.0
    Peso_acima = Peixe - 50
    print('vc devera pagar {}R$ de multa pelo {} com {}KG '.format (multa, especie ,Peixe))
    print('o peixe passou {:.1f}KG acima do limite que é 50KG'.format (Peso_acima))
else:
    Resto = 50 - Peixe
    print('vc não deve pagar multa por o peixe {} nao é maior que 50KG'.format (especie))
    print('o peixe ficou {}KG abaixo do limite'.format (Resto))
