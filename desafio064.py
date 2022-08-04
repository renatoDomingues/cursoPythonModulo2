#Crie um programa que leia "vários números" inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor "999", que é a "condição de parada". No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag).

'''
len() <=> Python list method len() returns the number of elements in the list.
'''
num = 0
count = 0
quant = 0

#FLAG:
num = int(input('Digite um número inteiro qualquer ou [999 para sair]: => '))
print(f'Você digitou acima o número {num}')
    
while num!=999:
    if num!=999:
        #variavel e contador:
    
        #count +=num
        count = count+num
    if quant!=999:
        quant = num
        quant = quant+1
    num = int(input('Digite um número inteiro qualquer ou [999 para sair]: => '))
    print(f'Você digitou acima o número {num}')

print(num, end=' SAIR=>\n')
#print(f'Você digitou {quant}') =>bug ao contar a digitação e menos o 999
print(f'A soma de todos os números acima, foram de {count}')
