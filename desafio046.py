# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles:
from time import sleep

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
print('Esse software faz uma contagem regressiva do número 10 ao 0:')

r= 10

print('Preparem se para uma contagem regressiva ...')
sleep(3)

'''
for c in range(10, -1, -1):
    print(c)
print('BUM! BUM!! POOW!! !!')
'''

for c in range(-1, 10):    
    print('{}'.format(r))
    sleep(1)
    r = r-1
    
print('BUM! BUM! POOW!! !! ...')

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
