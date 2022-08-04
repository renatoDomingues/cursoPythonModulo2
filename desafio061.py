#Refaça o "desafio051", lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while:

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

print('Como WHILE : :')
print('-=-' *10)
print('Gerador de PA')
print('-=-' *10)

prim = int(input('\nDigite um número inteiro do primeiro termo: =>'))
print('Você informou o número {} como primeiro termo!'.format(prim))
ra = int(input('Agora, digite um número inteiro da razão deste termo: =>'))
print('Você informou o número {} como a razão deste termo!'.format(ra))

termo = prim
cont = 1

while cont<=10:
    print('{} => '.format(termo), end='')
    #termo+=ra
    termo = termo+ra
    #cont+=1
    cont = cont+1

print(' ')
print('\nComo FOR : :')

pTermo = int(input('Informe um número inteiro como o primeiro termo: => '))
print('Você informou o número {} como primeiro termo!'.format(pTermo))
r = int(input('Agora, informe um número inteiro como a razão deste termo: => '))
print('Você informou o número {} como a razão deste termo!\n'.format(r))

#An = A1+(n-1)*R
termoGeral = pTermo+(10-1)*r

for c in range(pTermo, termoGeral+1, r):
    #print(c)
    print(c, end=' =>')
    
'''
prim = int(input('Digite um número inteiro do primeiro termo: =>'))
print('Você informou o número {} como primeiro termo!'.format(prim))
ra = int(input('Agora, digite um número inteiro da razão deste termo: =>'))
print('Você informou o número {} como a razão deste termo!'.format(ra))

contador = 1
resultado = prim
total = 0
a_mais = 10

while total!=10:
    total = total+a_mais
    print('Resultado: ', end='=>')
    while contador<=total:
        resultado = resultado+ra
        contador = contador+1
        print(resultado, end='<=>')
    
#print(contador)
print('\nVocê consultou {} termos.'.format(total))
'''

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
