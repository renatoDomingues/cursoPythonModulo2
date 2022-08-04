#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no íntervalo de 01 até 500:

print('\nEsse programa vai calcular a soma dos números ímpares que são multiplos de 03 em um intervalo de 01 até 500\n')
print('-=-'*10, 'START', '-=-'*10)

#Acumulador:
s = 0
#Contador:
quant =0

'''
for c in range(1, 501):
    print(c, end=' ')
'''
'''
for c in range(1, 501, 2):
    print(c, end=' ')
'''
'''
for c in range(1, 501, 2):
    if c%3==0:
        print(c, end=' ')
'''

for c in range(1, 500, 2):
    #print('Sociedade Esportiva Plameiras!!')
    if c%3==0:
        #s+=c
        s = s+c
        #quant+=1
        quant = quant+1
#print('Foram contados {} números e o resultados da soma de todos é {}'.format(quant, s))
print('A soma de todos são {}'.format(quant))
print('E os valores solicitados são {}'.format(s))
    
print('-=-'*10, 'END', '-=-'*10)
