#Melhore o jogo do "desafio028" onde o computador vai "pensar" em um "número entre 0 e 10". Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer:

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

from random import randint
from time import sleep

num = 0
comp = 1
v = 0

'''
acertou = False

while not acertou:
'''

while num!=comp:
    print('Digite um número inteiro de 0 a 10 abaixo')
    num = int(input('=> '))
    comp = randint(0, 10)
    sleep(0.5)
    #print('O computador pensou no número {}\n'.format(comp))
    if num<comp:
        print('MAIS ... ... Tente mais uma vez: ')
    elif num>comp:
        print('MENOS ... ... Tente mais uma vez: ')
    if num>10:
        print('ERRO desculpa, o número informado pelo usuário só é valido de 0 a 10.')
        print('Por favor, tente novamente ...')
    v = v+1
print('Foram necessarias {} vezes de chances ...'.format(v))
print('Parabéns, tu acertou!!')

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
