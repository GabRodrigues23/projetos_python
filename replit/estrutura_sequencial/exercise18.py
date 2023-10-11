# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

mb = float(input('Digite o tamanho do arquivo em MB: ').replace(',','.'))
mbps = float(input('Digite a velocidade da internet em MBPS: ').replace(',','.'))
tempo = mb / (mbps / 8)
print('{:.2f} segundos para o término do download'.format(tempo))