#Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem: -O primeiro valor é MAIOR; -O segundo valor é MAIOR; -Não existe valor maior, os dois são IGUAIS;

#import time
from time import sleep

print('O programa compara 02 números digitados, quem são maior ou os mesmos são iguais.')
#num1 = float(input('Digite o primeiro número inteiro: '))
num1 = int(input('Digite o primeiro número inteiro: '))
#num2 = float(input('Agora, digite o segundo número inteiro: '))
num2 = int(input('Agora, digite o segundo número inteiro: '))
print('Calculando, por favor espere um momento ...')
#time.sleep(4)
sleep(3)
print(' ')

if num1>num2:
    print('O primeiro número digitado acima {:.0f} é MAIOR do que o segundo número {:.0f} digitado.'.format(num1, num2))
    print('O número {:.0f} é MAIOR!!'.format(num1))
elif num2>num1:
    print('O segundo número digitado acima {:.0f} é MAIOR do que o primeiro número {:.0f} digitado.'.format(num2, num1))
    print('O número {:.0f} é MAIOR!!'.format(num2))
elif num1==num2:
    print('O primeiro número digitado acima {:.0f} é IGUAL ao o segundo número {:.0f} digitado.'.format(num1, num2))
    print('O número {:.0f} com o número {:.0f} são IGUAIS!!'.format(num1, num2))
else:
    print('ERRO, deculpa hoube um problema, \n por favor digite os 02 números inteiro novamente ...')
    
print(' ')
print('Obrigado ...')
print('FIM!!')
