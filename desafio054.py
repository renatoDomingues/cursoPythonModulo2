#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores:

#import date
from datetime import date

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
print('Esse programa irá ler o ano de nascimento de 07 pessoas e depois calcular os que atingiram a maioridade junto aqueles que não atingiram!\n')

anoAtual = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    anoMaior = int(input('Digite a data de nascimento, com 04 digitos como esse exemplo "1980" em que ano a {}° pessoa nasceu?  '.format(c)))
    #print('Você digitou a data de nascimento: {}'.format(anoMaior))
    if anoAtual-anoMaior>=18:
        #print('Pela a Constituição do Brasil, atingiram a maioridade!!')
        #maior+=1
        maior = maior+1
    else:
        #print('Pela a Constituição do Brasil, NÃO atingiram a maioridade!!')
        #menor+=1
        menor = menor+1
print('\nPela a nossa Constituição do Brasil vigente, {} pessoas acima digitadas que atingiram a maioridade e {} pessoas que não atingiram a maioriadade no nosso Brasil.'.format(maior, menor))
    
print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
