#Crie um programa que faça o computador jogar JOKENPÔ com você (pedra, papel e tesoura);

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
#print('O computador escolheu {}'.format(itens[computador]))

print('-START-'*10)
print(' ')
print('''
      SUAS OPÇÕES:
[0] PEDRA;
[1] PAPEL;
[2] TESOURA;
''')
jogador = int(input('Qual é a sua jogada? \n'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!! !!')
sleep(1)

print('-=-'*10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=-'*10)

if computador==0: #O computador jogou PEDRA
    if jogador==0:
        print('EMPATE')
    elif computador==1:
        print('O computador VENCE.')
    elif computador==2:
        print('O computador VENCE.')
    else:
        print('JOGADA INVÁLIDA!!')
elif computador==1: #O computador jogou PAPEL
    if jogador==0:
        print('O computador VENCE.')
    elif computador==1:
        print('EMPATE.')
    elif computador==2:
        print('O jogador VENCE.')
    else:
        print('JOGADA INVÁLIDA!!')
elif computador==2: #O computador jogou TESOURA
    if jogador==0:
        print('O jogador VENCE.')
    elif computador==1:
        print('O computador VENCE.')
    elif computador==2:
        print('EMPATE.')
    else:
        print('JOGADA INVÁLIDA!!')
        
print(' ')
print('-END-'*10)

'''
#import random
from random import randint

print('!!Tecnologia&Inovação DOMINGUES!! ' *2)
print(' ')
print('Esse sofware vai jogar JOKEMPÔ com você, "Pedra, Papel ou Tesoura".')
print('Está preparado!? ...')
print('Escolha abaixo somente as opções:\n -(1)Pedra;\n -(2)Papel;\n -(3)Tesoura; ')
escJok = int(input('=> '))
print('Você acabou de escolher a opção {}'.format(escJok))
print(' ')

comput = randint(1, 3)

if comput==escJok:
    print('EMPATE')
    print('Pois o computador escolheu a opção {} PEDRA e você também escolheu a opção {} PEDRA'.format(comput, escJok))
elif comput==1 and escJok==2:
    print('Você GANHOU!!')
    print('O computador escolheu a opção {} PEDRA e você escolheu {} PAPEL'.format(comput, escJok))
    print('Pois o papel ganha contra a pedra.')
elif comput==2 and escJok==1:
    print('Você PERDEU!!')
    print('O computador escolheu a opção {} PAPEL e você escolheu {} PEDRA'.format(comput, escJok))
    print('Pois o papel ganha contra a pedra.')
elif comput==2 and escJok==3:
    print('Você GANHOU!!')
    print('O computador escolheu a opção {} PAPEL e você escolheu {} TESOURA'.format(comput, escJok))
    print('Pois o papel perde contra a tesoura.')
elif comput==3 and escJok==2:
    print('Você PERDEU!!')
    print('O computador escolheu a opção {} TESOURA e você escolheu {} PAPEL'.format(comput, escJok))
    print('Pois o papel perde contra a tesoura.')
elif comput==1 and escJok==3:
    print('Você PERDEU!!')
    print('O computador escolheu a opção {} PEDRA e você escolheu {} TESOURA'.format(comput, escJok))
    print('Pois a pedra ganha contra a tesoura.')
elif comput==3 and escJok==1:
    print('Você GANHOU!!')
    print('O computador escolheu a opção {} TESOURA e você escolheu {} PEDRA'.format(comput, escJok))
    print('Pois a pedra ganha contra a tesoura.')
else:
    print('ERRO, houve um problema de digitação ao escolher as opções acima!! Por favor, tente novamente ...')
    
print(' ')
print('...FIM...'*10)
'''
