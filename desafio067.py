#Faça um programa que mostre a tabuada de varios números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo:

m = 0
#negative = 999

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

while True:
    n = int(input('\nDigite um número inteiro, para formular a sua tabuada OU para sair digite números negativos: '))
    
    if n<0:
        print('Tu digitou para sair ...')
        break
    
    print('-*-'*30)
    
    print(f'A tabuada do número {n} digitado acima, será: ')
    print('-*-'*30)
    for c in range(0, 11):
        m = n*c
        #print(f'{m}')
        #print(f'{m}', end=' ')
        print(n, 'X', c, '=', m)
        
    print('-*-'*30)
    
print('END!!')

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
