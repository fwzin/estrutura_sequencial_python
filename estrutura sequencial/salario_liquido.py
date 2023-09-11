"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário
no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa 
que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"""
print('')
print('Calculadora e salario bruto, IR, INSS, Sindicato, e o salario liquido')
print('')
Salario = float(input('quanto você ganha por hora: '))
Tempo = float(input('qual é o número de horas trabalhadas no mês: '))
print('')

SalarioBruto = (Salario * Tempo)
i = (SalarioBruto * 11) / 100
inss = (SalarioBruto * 8) / 100
Sindicato = (SalarioBruto * 5) / 100
Salario_liquido = (SalarioBruto - i - inss - Sindicato)

print('seu salario bruto é igual a: {}'.format (SalarioBruto))
print('foi descontado {}R$ para o IR'.format (i))
print('você pagou {}R$ de INSS'. format (inss))
print('você pagou {}R$ ao sindicato'.format (Sindicato))
print('do seu salario bruto de {}R$ restou {}R$ de salario liquido'.format (SalarioBruto, Salario_liquido))
