#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: -1- para binário -2- para octal -3- para hexadecimal;

print('A função do programa é de converção para "BINÁRIO", "OCTAL" e "HEXADECIMAL"')
#num = int(input(''' Escolha uma das bases para conversão:
# [1] Converter para BINÁRIO;
# [2] Converter para OCTAL;
# [3] Converter para HEXADECIMAL; '''))
print('Digite um número inteiro qualquer abaixo: ')
num = int(input('=> '))
print(' ')
print('O número digitado acima, você vai escolher \n (1)-BINÁRIO \n (2)-OCTAL \n (3)-HEXADECIMAL \n Por favor digite abaixo somente 1, 2 ou 3:')
conv = int(input('=> '))
print(' ')

if conv==1:
    #print('O número digitado acima foi {} porém a converção escolhida será para {} Binário.'.format(num, bin(num)))
    print('O número digitado acima foi {} porém a converção escolhida será para {} Binário.'.format(num, bin(num)[2:]))
elif conv==2:
    #print('O número digitado acima foi {} porém a converção escolhida será para {} Octal.'.format(num, oct(num)))
    print('O número digitado acima foi {} porém a converção escolhida será para {} Octal.'.format(num, oct(num)[2:]))
elif conv==3:
    #print('O número digitado acima foi {} porém a converção escolhida será para {} Hexadecimal.'.format(num, hex(num)))
    print('O número digitado acima foi {} porém a converção escolhida será para {} Hexadecimal.'.format(num, hex(num)[2:]))
else:
    print('ERRO, desculpa houve um problema na escolha do seu número acima ou pelas suas escolhas das opções disponiveis!\nPor favor, tente de novo ...')
    
