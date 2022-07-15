#Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado..

#print(*20 'Domingues Bank' *20)
print('Domingues Bank')
print('SEJA BEM VINDO!! O seu sonho preste a ser realizado e ficamos honrados de fazer parte disso.')
print(' ')

emp = float(input('Por favor, digite o valor do emprestimo desejado: R$'))
print('Você digitou o valor desejado a financiar R${:.2f} reais'.format(emp))
sal = float(input('Por favor, agora o valor do seu salário atual: R$'))
print('O valor digitado acima do seu salário foi R${:.2f} reais'.format(sal))
div = float(input('Por ultimo, em quantas vezes"meses" tu deseja pagar o seu imovél: '))
#anos = int(input('Por ultimo, em quantas vezes"anos" tu deseja pagar o seu imovél: '))
print('Você acabou de digitar quantidades de meses a pagar {:.0f}'.format(div))

empDiv = emp/div
apro30 = (sal*30)/100
#if sal*0.3>empDiv:
#prest = emp/(anos*12) 
#min = sal*30/100
parc = emp/div 

print('\n O valor do emprestimo pedido acima de R${} reais em {:.0f} meses para pagar, as suas parcelas será R${:.2f} reais\n'.format(emp, div, parc))

#if sal*0.3>empDiv:

if parc <= apro30:
    print('PARABÊNS, o seu sonho da sua compra, financiamento seu imovel está mais proximo!')
    print('Pelo nosos sistema, as informações digitadas acima, está pré aprovado o seu pedido. Por favor, procure um gerente em uma das nossas agencias, para melhores análises e para assinar o seu contrato')
    print('OBRIGADO pela a sua confiancia ...')
else:
    print('DESCULPE, pela a nossa primeira análise baseado nas informações digitadas acima!?')
    print('No momento, seu pedido credito foi negado!')
    print('OBRIGADO pela a sua confiancia ...')
    
print(' ')
print('Domingues Bank')
 