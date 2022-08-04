#Crie um programa que leia dois valores e mostre um menu na tela: [1]somar; [2]multiplicar; [3]maior; [4]novos números; [5]sair do programa; Seu programa deverá realizar a operação solicitada em cada caso.

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

menu = 0
#maior =0
#menor = 0

while menu!=5:
    n1 = int(input('\nDigite um número: '))
    n2 = int(input('Agora digite o segundo número: '))
    print('Escolha uma das opções abaixo:')
    menu = int(input('''
                     [1]Somar; 
                     [2]Multiplicar; 
                     [3]Maior; 
                     [4]Novos números; 
                     [5]Sair; 
                     =>
                     '''))
    if menu==1:
        so = n1+n2
        print('A soma dos números {} e {} digitados acima, foram {}'.format(n1, n2, so))
    if menu==2:
        mu = n1*n2
        print('A multiplicação dos números {} e {} digitados acima, foram {}'.format(n1, n2, mu))
    if menu==3:
        if n1>n2:
            #maior = n1
            print('O menor dos números {} e {} digitados acima, foi {}'.format(n1, n2, n1))
        elif n1==n2:
            print('Os números {} e {} digitados acima, são iguais'.format(n1, n2))
        else:
            #menor = n2
            print('O maior dos números {} e {} digitados acima, foi {}'.format(n1, n2, n2))
    if menu==4:
        print('Você cancelou os 02 números já digitados acima')
        print('Por favor, digite novamente ...\n')
    elif menu!=1 and menu!=2 and menu!=3 and menu!=4 and menu!=5:
        print('ERRO desculpa, o número e a opção digitada do menu acima! Tente novamente ...')

print('END!! !!')

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
