#Crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar quando digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag):

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

n = soma = quant =0

while True:
    
    n = int(input('Por favor digite um número inteiro e caso quiser sai digite 999: '))
    
    if n==999:
        print('Tu acabou de digitar "999" para sair!')
        break
    #n+=1
    #n-=999
    quant +=1
    soma +=n
  
print(f'\nA quantidade dos números que foram digitados a cima foram {quant}')  
print(f'A soma dos números que foram digitados a cima foram {soma}')  
print('END!!')

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
