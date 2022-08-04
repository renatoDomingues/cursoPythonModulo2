#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos:

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
print('Esse sofware vai ler os pesos de 05 pessoas e mostrará na tela o maior e menor peso!')

'''
maior = 0
menor = 1000
'''
maior = 0
menor = 0

'''
for c in range(1, 6):
    print('Digite o peso abaixo: ')
    peso = float(input('O peso da {}° pessoa => '.format(c)))
    if peso>maior:
        maior=peso
    elif peso<menor:
        menor=peso
print('\nO maior peso foi {}Kg, sendo o menor peso foi {}Kg'.format(maior, menor))
'''
print('Digite os pesos abaixo: ')

for c in range(1, 6):
    peso = float(input('O peso da {}° pessoa => '.format(c)))
    if c==1:
        maior = peso
        menor = peso 
    else:
        if peso>maior:
            maior = peso
        if peso<menor:
            menor = peso
print('\nO maior peso foi {}Kg, sendo o menor peso foi {}Kg'.format(maior, menor))
    
print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
