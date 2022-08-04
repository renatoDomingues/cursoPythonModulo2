#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto:

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')

'''
.strip() <=> é eliminar contar espaços;
.upper() <=> print só letras maiusculas;
.upper()[0] <=> print só letras maiusculas e junto só pega a primeira letra digitada;
'''

'''
while sexo not in 'MmFf':
'''

sexo =' '

while sexo!='M' and sexo!='F':
    print('Digite o seu sexo abaixo: ')
    sexo = str(input('[M/F]=> ')).strip().upper()[0]
    if sexo!='M' and sexo!='F':
        print('Desculpa ERRO, por favor digite novamente!')
print('\nVocê digitou o sexo {}'.format(sexo))
if sexo=='M':
    masc = 'masculino'
    print('Do sexo {}, registrado com sucesso.'.format(masc))
else:
    fem = 'feminino'
    print('Do sexo {}, registrado com sucesso.'.format(fem))
    
print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
