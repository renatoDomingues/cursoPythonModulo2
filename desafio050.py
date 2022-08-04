#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o:

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

print('Esse programa irá pedir 06 números inteiros, que irá somar todos aqueles que forem pares e ignorando os ímpares!\n')
print('Por favor, você irá digitar 06 números inteiros, um por um abaixo: ')
#n1 = int(input('Digite o primeiro número inteiro: '))
#n2 = int(input('Digite o segundo número inteiro: '))
#n3 = int(input('Digite o terceiro número inteiro: '))
#n4 = int(input('Digite o quarto número inteiro: '))
#n5 = int(input('Digite o quinto número inteiro: '))
#n6 = int(input('Agora e por ultimo, digite o sexto número inteiro: '))
#print('Você acabou de digitar acima os números {}, {}, {}, {}, {} e {} como números inteiros'.format(n1, n2, n3, n4, n5, n6))

#Acomulador:
s = 0
#Contagem:
cont = 0

for c in range(1, 7):
    #n = int(input('Por favor, digite um número inteiro qualquer: '))
    n = int(input('Digite o {}° valor: '.format(c)))
    if n%2==0:
        #s+=n
        s = s+n
        #cont+=1
        cont = cont +1

print('Você informou {} números pares acima'.format(cont))
print('Sendo a soma destes números pares foram {}'.format(s))

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
