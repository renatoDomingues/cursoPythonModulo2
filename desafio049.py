#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for:

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

print('Esse sofware vai pedir um número para demonstrar no visor a sua tabuada\n')
print('Digite um número inteiro qualquer abaixo:')
nTabu = int(input('=> '))
print('Você digitou o número {} acima.'.format(nTabu))
print('A tabuada do número {} será formada abaixo ...\n'.format(nTabu))

quant = 0
m= 0

'''
for c in range(1, 11):
    print('{} X {:2} = {}'.format(nTabu, c, nTabu*c))
    #print('{} X {} = {}'.format(nTabu, c, nTabu*c))
'''

print('-=-'*4, 'START', '-=-'*4)
for c in range(0, 11):
    #print('Sociedade Esportiva PaLmeiras!')
    #quant = quant+1
    #s+=c
    m = nTabu*c
    
    #print(nTabu, 'X', quant, '=', m)
    print(nTabu, 'X', c, '=', m)
print('-=-'*4, 'END', '-=-'*4)
    
print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
