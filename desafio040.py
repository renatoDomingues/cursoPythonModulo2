#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: -Média abaixo de 5.0: REPROVADO; -Média entre 5.0 e 6.9: RECUPERAÇÃO; -Média 7.0 ou superior: APROVADO;

print('Esse sofware vai ler as 02 notas de um aluno, para fazer a média se o mesmo foi aprovado, recuperação ou reprovado.')
print('Digite as suas 02 notas abaixo')
print(' ')
print('Qual a sua primeira nota: ')
not1 = float(input('=> '))
print('Qual a sua segunda nota: ')
not2 = float(input('=> '))
print('Você digitou acima as suas 02 notas, sendo a primeira {} e a segunda {}\n'.format(not1, not2))

media = (not1+not2)/2

if media>=7:
    print('A sua média foi {}'.format(media))
    print('PARABÉNS, pois você foi APROVADO!!')
elif media>=5 and media<7:
    print('A sua média foi {}'.format(media))
    print('Sinal AMARELO,\nprecisa mais atenção e estudo, \n pois você foi para RECUPERAÇÃO!!')
else:
    print('A sua média foi {}'.format(media))
    print('INFELIZMENTE,\nvocê foi REPROVADO!!')
