#Sobre WHILE:
'''
print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

cont = 1

print('Start', end=' ')
while cont<=10:
    print(cont, '<=>', end='')
    cont+=1
print('End')

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
'''

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n') 

n = s = 0

while True:
    n = int(input('Digite um número: '))
    if n==999:
        break
    s+=n

print(f'\nA soma vale {s}')

nome = 'José'
idade = 33

print(f'O {nome} tem {idade} anos.') #Python3.6
print('O {} tem {} anos.'.format(nome, idade)) #Python3
print('O %s tem %d anos.' % (nome, idade)) #Python2

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

'''
n = s = 0

while n!=999:
    n = int(input('Digite um número: '))
    s+=n
s-=999
print(f'\nA soma vale {s}')
'''

'''
n = cont = 0

while cont<3:
    n = int(input('Digite um número: '))
    cont+=1
'''

'''
print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

cont = 1

print('Start', end=' ')
while True:
    print(cont, '<=>', end='')
    cont+=1
print('End')

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
'''
