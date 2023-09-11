"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
print('')
arquivo = float(input('qual é o tamanho de um arquivo para download (em MB): '))
tempo = float(input('qual é a velocidade de um link de Internet (em Mbps): '))

tamanho_mb = arquivo * 8
vel_mbps = tempo / 8
tempo_seg = tamanho_mb / vel_mbps
tempo_min = tempo_seg / 60

print('')
print('velocidade do arquivo será de {}'.format (tempo_min))





