#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: (A)quantas pessoas tem mais de 18 anos; (B)quantos homens foram cadastrados; (C)quantas mulheres tem menos de 20 anos;

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

h = m = m20 = p =0

while True:
    i = int(input('Com números inteiros, informe a idade: '))
    s = str(input('Informe o sexo, somente com as letras [M/F]: ')).upper()[0].strip()
    #print(f'Você informou a idade {i} anos e o sexo {s}')
    if s!='M' and s!='F':
        print('Na proxima tentativa:')
        print('ERRO na digitação, por favor na opção digite somente M para masculino ou F para feminino ...')
        break
    if s=='M':
        print(f'Você informou a idade de {i} anos e o sexo {s} de masculino.')
        h +=1
    if s=='F':
        print(f'Você informou a idade de {i} anos e o sexo {s} de feminino.')
        m +=1
    if i<20:
        if s=='F':
            m20 +=1            
    
    cont = str(input('Deseja continuar, digite somente [S/N]: ')).upper()[0].strip()
    print(' ')
    if cont!='S' and cont!='N':
        print('Na proxima tentativa:')
        print('ERRO na digitação, por favor na opção digite somente S para continuar ou N para não continuar ...')
        break
    if i>18:
        #p +=i
        #p = i
        p +=1
        
    if cont=='N':
        print('Você digitou a opção SAIR ...')
        break
    
print(f'\nNo total dos cadastrados acima, tem {p} pessoas maiores de 18 anos.')
print(f'No total dos cadastrados acima, tem {h} pessoas cadastradas como sexo masculino e {m} pessoas como sexo feminino.')
print(f'No total com {m20} mulheres menores de 20 anos.')
print('END!!')

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

'''
while resp not in 'SN':
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
if resp=='N':
    print('Tu digitou a letra N para não continuar ...')
    break
'''
