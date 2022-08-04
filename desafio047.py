#Um número pode ser considerado par ou ímpar. Os números pares são aqueles terminados em 0, 2, 4, 6 ou 8, já os ímpares são números terminados em 1, 3, 5, 7 ou 9.
#Os números pares são aqueles divisíveis por 2. Ou seja, se dividirmos um número por 2 e o resto da divisão for zero, trata-se de um número par. Um número é considerado ímpar se ele não for divisível por 2, isto é, se dividirmos esse número por 2 e ele deixar um resto igual a 1. Dito isso ...
#Crie um programa que mostre na tela todos os números pares que estão no intervalo entree 1 ao 50: 

from time import sleep

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

'''
for c in range(2, 51, 2):
    print(c, end=' ')
print('Acabou')
'''
'''        
for c in range(1, 51):
    print('.', end=' ')
    if c%2==0:
        print(c, end=' ') 
'''

n = 0

print('Os números pares entre 1 ao 50 são: \n')
sleep(1)

for c in range(1, 51):
    '''
    print('{}'.format(n))
    sleep(0.3)
    n = c+1
    '''
    if c%2==0:
        print('{}'.format(c))
        sleep(0.3)

print('Acabou!!')

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
