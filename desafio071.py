#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS=Considere que o caixa possui cédulas de R$50,00 reais, R$20,00 reais, R$10,00 reais e R$01,00 real:

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

print('-*-'*30)
print('{:^10}'.format('$B&D$ - BankDomingues - $B&D$'))
print('-*-'*30)

valor = int(input('Que valor tu quer sacar? R$'))
total = valor

ced = 50
totCed = 0

while True:
    if total>=ced:
        total-=ced
        totCed+=1
    else:
        if totCed>0:
            print(f'Total de {totCed} cédulas de R${ced} reais.')
        if ced==50:
            ced =20
        elif ced ==20:
            ced =10
        elif ced ==10:
            ced =1
        totCed =0
        if total==0:
            break
        
print('-*-'*30)
print('Obrigado pela preferencia e volte sempre.')
print('{:^10}'.format('$B&D$ - BankDomingues - $B&D$'))
print('END!!')

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
