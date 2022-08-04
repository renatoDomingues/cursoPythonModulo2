#Melhore o "desafio061", perguntando para o usuário se ele quer mostrar mais alguns termos. programa encerra quando ele disser que quer mostrar 0 termos:

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

print('-=-' *10)
print('Gerador de PA')
print('-=-' *10)
print(' ')

primeiro = int(input('Primeiro termo: '))
razao = int(input('A Razão da PA: '))

termo = primeiro
cont = 1
total = 0
mais = 10

while mais!=0:
    total = total+mais
    while cont<=total:
        print('{} => '.format(termo), end='')
        #termo+=razao
        termo = termo+razao
        #cont+=1
        cont = cont+1
    print('PAUSA ...')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados acima.'.format(total))
print('END!!')

'''
primTerm = int(input('Digite um número inteiro para o primeiro termo: =>'))
ra = int(input('Digite um número inteiro para a sua razão do termo: =>'))

cont = 1
res = primTerm
total = 0
ra_mais = 10

while ra_mais!=0:
    total = total+ra_mais
    print('O resultado: ', end='=>')
    while cont<=total:
        res = res+ra
        cont = cont+1
        print(res, end='<=>')
    ra_mais = int(input('\nTu quer mais termos para mostrar? '))
#print(cont)
print(f'Obrigado, pois tu consultou {total} termos.')
'''

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
