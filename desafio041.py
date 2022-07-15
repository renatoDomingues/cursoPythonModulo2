#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: -At´9 anos: MIRIM; -Até 14 anos: INFANTIL; -Até 19 anos: JUNIOR; -Até 20 anos: SENIOR; -Acima 20 anos: MASTER;

from datetime import date
from operator import iadd
#import time
from time import sleep

print('Esse sofware vai analisar com o seu dados, como o ano de nascimento, para saber em qual competição de natação irá concorrer.')
print('Confederação Nacional de Natação')
print('Ensira abaixo o seu ano com 04 digitos de nascimento: ')
nascim = int(input('=> '))
print('Você digitou acima o seu ano de nascimento {}.'.format(nascim))
print(' ')

#anoAtual = date.today().year-ano
atual = date.today().year
idade = atual-nascim

print('Você tem {} anos'.format(idade))
#time.sleep(3)
sleep(3)

if idade<=9:
    print('Você como candidato será destinado para a categoria MIRIM.')
elif idade>9 and idade<=14:
    print('Você como candidato será destinado para a categoria INFANTIL.')
elif idade<=20:
    print('Você como candidato será destinado para a categoria JUNIOR.')
elif idade<=25:
    print('Você como candidato será destinado para a categoria SENIOR.')
elif idade<=120:
    print('Você como candidato será destinado para a categoria MASTER.')
elif idade==0 and idade>120:
    print('DESCULPA, mas não é possivel competir com essa idade!!')
else:
    print('ERRO, desculpa algum problema na sua digitação, por favor tente de novo ...')
