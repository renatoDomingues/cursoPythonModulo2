#Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5!=5X4X3X2X1=120

#from math import factorial

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
'''
n!= n*(n-1)*(n-2) ...*3*2*1 
4!= 4X3X2X1=24
5!= 5X4X3X2X1=120 OU 5!= 5X4!=5X24=120
'''

print('Com WHILE:')
print('Digite um número inteiro qualquer abaixo, para encontrarmos o seu fatorial!.')
numWhile = int(input('=> '))
print('Você digitou acima o número {}\n'.format(numWhile))

resWhile = 1
countWhile = 1

while countWhile<=numWhile:
    #resWhile*=countWhile
    resWhile = resWhile*countWhile
    #countWhile+=1
    countWhile = countWhile+1    
    print(resWhile)
    
print('\nCom FOR:')
print('Digite um número inteiro qualquer abaixo, para encontrarmos o seu fatorial!.')
numFor = int(input('=> '))
print('Você digitou acima o número {}\n'.format(numFor))

resFor = 1

for c in range(1, numFor+1):
    #resFor*=c
    resFor = resFor*c
    print(resFor)


print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
