#Desenvolva um programa que leia o nome, idade e sexo de 04 pessoas. No final do programa, mostre: A média de idade do grupo; Qual é o nome do homem mais velho; Quantas mulheres têm menos de 20 anos;

#from datetime import date

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
print('O programa irá ler o nome, sexo e a idade de 04 pessoas, sendo que calculará a média de idade do grupo, o homem mais velho e a mulher com menos de 20 anos.')

somaIdade = 0
mediaIdade = 0
#anoAtual = date.today().year
maioridadeHomem = 0
nomeVelho = ''
totMulher20 = 0

for c in range(1, 5):
    print('-=-'*2, '{}° PESSOA'.format(c), '-=-'*2)
    nome = str(input('Digite o nome: ').upper())
    idade = int(input('Agora, digite a idade: '))
    sexo = str(input('Por ultimo digite o sexo por apenas [M/F]: ').upper())
    #print('Você digitou o nome {}, com a idade {} e o sexo {}'.format(nome, idade, sexo))
    #somaIdade+=idade
    somaIdade = somaIdade+idade
    if c==1 and sexo in 'M':
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'M' and idade>maioridadeHomem:
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'F' and idade<20:
        #totMulher20+=1
        totMulher20 = totMulher20+1
    
mediaIdade = somaIdade/4
print('\nA média de idade do grupo é de {} anos'.format(mediaIdade))
print('\nO homem mais velho tem {} anos e se chama {}'.format(maioridadeHomem, nomeVelho))
print('\nAo todo são {} mulheres com menos de 20 anos'.format(totMulher20))

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
    