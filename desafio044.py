#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: -Á vista dinheiro/cheque: 10% de desconto; -Á vista no cartão: 5% de desconto; -Em até 2X no cartão: preço normal; -3X ou mais no cartão: 20% de juros;

print('!!Tecnologia&Inovação DOMINGUES!! ' *2)
preco = float(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTOS
[1]à VISTA em dinheiro/cheque;
[2]à VISTA CARTÃO;
[3]em 2X no CARTÃO s/ juros;
[4]em 3X ou MAIS no CARTÃO CREDITO;     
''')
opcao = int(input('Qual é a opção: '))
print('Você digitou acima o preço R${} reais das suas compras e com a opção {} desejada a pagar.'.format(preco, opcao))

if opcao==1:
    #total = preco-((preco*10)/100)
    desc = (preco*10)/100
    total = preco-desc
    parcJur =total
    print('O seu desconto foi de R${:.2f} reais\n'.format(desc))
elif opcao==2:
    desc = (preco*5)/100
    total = preco-desc
    parcJur =total
    #total = preco-((preco*5)/100)
    print('O seu desconto foi de R${:.2f} reais\n'.format(desc))
elif opcao==3:
    total = preco
    parc2 = total/2
    parcJur =total
    print('Sua compra será parcelada em 2X vezes de R${:.2f}\n'.format(parc2))
elif opcao==4:
    total = (preco*20)/100
    parcJur = preco+total
    totParc = int(input('Quantas parcelas? '))
    print('Você digitou {} parcelas, sendo terá um acrescimos de R${} reais\n'.format(totParc, total))
    parc = parcJur/totParc
    print('A sua compra será parcelada em {} de R${:.2f} reais'.format(totParc, parc))
else:
    total = preco
    parcJur = total
    print('ERRO, opção INVÁLIDA de pagamento. Por favor, tente novamente!\n')
    
print('Sua compra de R${:.2f} reais vai custar R${:.2f} reais\n'.format(preco, parcJur))

print('!!Tecnologia&Inovação DOMINGUES!! ' *2)

'''
print('!!Tecnologia&Inovação DOMINGUES!! ' *2)
print(' ')
vlorProd = float(input('Por favor, passe ou digite o codigo barra do produto desejado: R$'))
print('O valor deste produto X acima R${:.2f} reais.'.format(vlorProd))
print('Qual é a forma de pagamento que deseja pagar:\n -(1)Á vista com 10% de desconto;\n -(2)Á vista no cartão credito com 5% de desconto;\n -(3)Em até 2X no seu cartão de credito com o preço normal;\n -(4)Ou 3X ou mais vezes no seu cartão de credito, mas com 20% de juros;\n DIGITE somente as opções: 1, 2, 3 ou 4 abaixo:')
pgto = int(input('=> '))
print('Você digitou a opção {} como modo de pagamento.'.format(pgto))

#vista10 = pgto-((pgto*10)/100)

if pgto==1:
    descVistaDinh = (vlorProd*10)/100
    vista10 = vlorProd-descVistaDinh
    print('Você escolheu a pagar a vista no dinheiro ou no cheque com 10% de desconto de R${:.2f} reais, que seu produto ficará por R${:.2f} reais.'.format(descVistaDinh, vista10))
elif pgto==2:
    descVistaCart = (vlorProd*5)/100
    vista5 = vlorProd-descVistaCart
    print('Você escolheu a pagar a vista no cartão de debito ou no credito em 01X, com 5% de desconto de R${:.2f} reais, que seu produto ficará por R${:.2f} reais.'.format(descVistaCart, vista5))
elif pgto==3:    
    vistaNorm = vlorProd/2
    print('Você escolheu a pagar em até 02X no seu cartão de credito, com preço normal do produto de R${:.2f} reais, que seu produto ficará por R${:.2f} reais parcelados em 02 vezes.'.format(vlorProd, vistaNorm))
elif pgto==4:
    juros20 = (vlorProd*20)/100
    parcJuros20 = vlorProd+juros20
    print('Você escolheu a pagar em parcelados de 03X ou mais vezes, que seu produto de R${:.2f} reais, terá um aumento de R${} reais.'.format(vlorProd, parcJuros20))
else:
    print('ERRO, desculpa teve um problema na digitação das opções do modo do pagamento! Por favor, tente novamente ...')
    
print(' ')
print('Obrigado pela confiança')
'''
