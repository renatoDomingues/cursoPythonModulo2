#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo:

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
print('Esse sofware irá pedir que digite um número inteiro, para dar a resposta se é ou não número primo! O número PRIMO é/ou são os números naturais que podem ser divididos por apenas dois fatores: o número um e ele mesmo.')
numPrimo = int(input('Digite um número inteiro qualquer: '))
print('Você digitou acima o número {}\n'.format(numPrimo))

#Variavel:
tot = 0

for c in range(1, numPrimo+1):
    if numPrimo%c==0:
        #print('\033[33m', end='')
        print(' "Foi divisível"!', end='=> ')
        #tot +=1
        tot = tot+1
    else:
        #print('\033[31m', end='')
        print(' "não foi divisível"!', end='=> ')
    #print('\n{}'.format(c), end=' ')
    print('{}'.format(c))
    
print('\nO número {} foi divisível {} vezes'.format(numPrimo, tot))

if tot==2:
    print('E por isso o mesmo é PRIMO!!')
else:
    print('E por isso o mesmo NÃO é PRIMO!!')

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
