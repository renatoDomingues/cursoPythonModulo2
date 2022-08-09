#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo:

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

from random import randint

comp = randint(0, 11)
#print(comp)
s = v =0

while True:
    print('PAR ou ÍMPAR, digite P para PAR ou I para ÍMPAR? ...')
    parImpar = str(input('[P/I] => ')).upper().strip()
    #print(parImpar)
    print('Baseado com a sua escolha acima, digite um número inteiro de 0 a 10? ...')
    n = int(input('[0/10] => '))
    s = comp+n
    div = s/2
    #print(s)
    #print(div)
    if parImpar!='P' and parImpar!='I':
        print('ERRO na digitação, por favor na opção digite somente a letra P ou I')
        print(f'O comparador jogou {comp} e tu jogou {n}.\n')
    if div%2==0:
        print(f'O calculo entre sua escolha e a do computador foi {div}, pois é PAR!')
        print(f'O comparador jogou {comp} e tu jogou {n}.\n')
    else:
        print(f'O calculo entre sua escolha e a do computador foi {div}, pois é IMPAR!')
        print(f'O comparador jogou {comp} e tu jogou {n}.\n')
    if parImpar=='P' and div%2==0:
        print('Tu ganhou!!')
        v +=1
    else:
        print('Tu perdeu!!')
        break

print(f'A soma das suas vitórias foram {v}.')
print('END!!')

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
