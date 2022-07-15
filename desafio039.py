#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: -Se ele ainda vai se alistar ao serviço militar; -Se é a hora de se alistar; -Se já passou do tempo do alistamento; Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo.

#import datetime
from datetime import date

print('Empresa Startup Domingues Tecnologia!')
print('Programa de alistamento baseado com sua idade ...')
print(' ')
print('Digite a data do seu nascimento')
print('Qual é o ano do seu nascimento abaixo:')
nasc = int(input('=> '))
print('Qual é o seu sexo, apenas digite "F" para feminino ou "M" para masculino:')
sexo = str(input('=> ')).upper()

atual = date.today().year
idade = atual - nasc

calIdade = date.today().year-nasc

print('O seu ano de nascimento digitado acima foi {} ano.'.format(nasc))
print('Quem nasceu no ano {} na data de hoje, tem uma idade de {} anos.'.format(nasc, calIdade))
if sexo=='F':
    print('Para a opção do seu sexo, você digitou {} para feminino!'.format(sexo))
else:
    print('Para a opção do seu sexo, você digitou {} para masculino!'.format(sexo))
print(' ')

if calIdade<18:
    saldo = 18-idade
    ano = atual+saldo
    print('Olá,\nvocê ainda não precisa se alistar nas nossas Forças Armadas!!')
    print('Daqui em {} anos você deverá se alistar.'.format(18-calIdade))
    print('O seu alistamento será em {}'.format(ano))
elif sexo=='F' and calIdade==18:
    print('Não é obrigatorio o alistamento nas Forças Armadas brasileiras para mulheres.\nCaso tenha interesse: ')
    print('PARABÉNS pelo seu PATRIOTISMO!!\nVocê já está com a idade de se apresentar em uma das bases/juntas mais proximas das nossas Forças Armadas!!')
elif calIdade==18:
    print('PARABÉNS pelo seu PATRIOTISMO!!\nVocê já está com a idade de se apresentar em uma das bases/juntas mais proximas das nossas Forças Armadas!!')
    print(' ')
elif calIdade>18:
    saldo = idade-18
    ano = atual-saldo
    print('Você já passou do tempo do seu alistamento, pois se apresente o mais rapido possivel em uma base/junta mais proxima para maiores informações!')
    print('O seu tempo de se alistar, seria em {} anos atrás.'.format(calIdade-18))
    print('O seu alistamento deveria ser no ano {}'.format(ano))
else:
    print('ERRO, houve um problema na sua digitação sobre sua data de nascimento ...\nPor favor, digite novamente ...')
    
    print('OBRIGADO pela a confiança')
