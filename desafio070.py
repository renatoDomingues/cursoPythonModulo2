#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: (A)qual é o total gasto na compra; (B)quantos produtos custam mais de R$1000,00 reais; (C)qual é o nome do produto mais barato;

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

t = g = acima = mais = menos = 0

while True:
    n = str(input('Insira o nome do produto desejado? ')).upper()
    p = int(input('Em números inteiro, digite o valor que consta na embalagem deste produto: R$'))
    print(f'Você digitou o nome: {n} e com valor: R${p:.2f} reais.')
    
    o = str(input('\nDeseja sair? S para sair ou N para continuar [S/N]: ')).upper().strip()
    if o!='S' and o!='N':
        print('ERRO desculpa, digite a opção S para SAIR ou N para NÃO sair, correto na próxima vez!')
        print('A opção errada acima, consideramos que queira continuar.\n')
    
    if p>0:
        t +=1 #gera quantidades da soma dos produtos
        g = g+p #gera o valor acumulado em preços reais
    if t==1:
        mais = menos = p
    else:
        if p>mais:
            mais=p
        if p<menos:
            menos=p            
    if p>1000:
        acima +=1 #acima do valor R$1000
    
    if o=='S':
        print('Você escolheu a opção SAIR ...')
        break
    
print(f'\nNo total acima foram {t} compras efetuadas.')
print(f'Cadastrados {acima} produtos acima do valor de R$1.000,00 reais')
print(f'O produto escolhido mais barato foi de R$ {menos} reais')
print('Já o total gasto das compras acima, foram de R${:.2f} reais'.format(g))
print('END!!')

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

'''
while resp not in 'SN':
    rep = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
if resp=='N':
    break
    
print('{:-^40}'.format('FIM DO PROGRAMA'))
'''
