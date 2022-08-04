#Desenvolva um programa que leia o primeiro termo de uma PA. No final, mostre os 10 primeiros termos dessa progressão:

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
print('Esse programa irá ler o primeiro termo de uma PA "PROGRESSÃO ARITMÉTICA é uma sequência numérica em que cada termo, a partir do segundo, é igual à soma do termo anterior com uma CONSTANTE R. O número R é chamado de RAZÃO ou diferença comum da progressão aritmética", sendo no final a tela mostrará os 10 primeiros termos dessa progressão.\n')

print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

print('Por favor informe o primeiro termo da PA abaixo: ')
a = int(input('PA => '))
print('Agora, informe a razão abaixo: ')
r = int(input('RAZÃO => '))

#An = A1+(n-1)*R
termoGeral = a+(10-1)*r

'''
#for c in range(primeiroTermo, 10, razão):
for c in range(1, 10, 1):
    print('{}'.format(c), end='=> ')
print('ACABOU')
'''
'''
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

decimo = primeiro+(10-1)*razao

for c in range(primeiro, decimo+razao, razao):
    print('{}'.format(c), end='=> ')
print('END!!')
'''

for c in range(a, termoGeral+1, r):
    #print(c)
    print(c, end=' -> ')
print('END!!')

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
