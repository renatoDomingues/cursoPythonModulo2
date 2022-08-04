#Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5!=5X4X3X2X1=120; COM repetição WHILE:

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

from math import factorial
'''
#Com ajuda do Python:
n = int(input('\nDigite um número para calcular o seu Fatorial!: '))
f = factorial(n)
print('\nO Fatorial! de {} é {}.'.format(n, f))
'''
n = int(input('\nDigite um número para calcular o seu Fatorial!: '))
#variaveis:
c = n
f = 1

print('Calculando {}! <=> '.format(n), end='')

while c>0:
    #print('{}'.format(c))
    print('{} '.format(c), end='')
    #print('X ' if c>1 else '= ', end='')
    if c>1:
        print('X ', end='')
    else:
        print('= ', end='')
    #f*=c
    f = f*c
    c-=1
print('{}'.format(f))

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
