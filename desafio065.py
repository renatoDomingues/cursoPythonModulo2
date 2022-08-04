#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores:

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

resp = 'S'
media = quant = soma = maior = menor =0

while resp in 'Ss':
    num = int(input('Digite um número: '))    
    #soma+=num
    soma = soma+num
    #quant+=1
    quant = quant+1
    if quant==1:
        maior = menor = num
    else:
        if num>maior:
            maior =num
        if num<menor:
            menor =num
    
    resp = str(input('Que continuar? [S/N] ')).upper().strip()[0]
media = soma/quant
    
print(f'Você digitou {quant} números e a média foi {media}')
print(f'O maior valor foi {maior}, sendo o menor valor foi {menor}')
print('End !!')
        
print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
