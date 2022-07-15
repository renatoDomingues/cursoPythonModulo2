nome = str(input('Qual é o seu nome? ')).upper()

#CEstrutura Condicional SIMPLES abaixo:
'''
if nome == 'RENATO':
    print('Que nome bonito!!')
'''
    
#Estrutura Condicional COMPOSTA abaixo:
'''
if nome == 'RENATO':
    print('Que nome bonito!!')
else:
    print('Seu nome é bem normal.')
'''
#Estrutura Condicional ANINHADA abaixo:
'''
if nome == 'RENATO':
    print('Que nome bonito!!')
elif nome=='PEDRO' or nome=='MARIA' or nome=='PAULO':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
'''

#Estrutura Condicional ANINHADA abaixo:
if nome == 'RENATO':
    print('Que nome bonito!!')
elif nome=='PEDRO' or nome=='MARIA' or nome=='PAULO':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'ANA CLAUDIA JESSICA JULIANA':
    print('Belo nome feminino!!')
else:
    print('Seu nome é bem normal.')
    
#else <=> é opcional
    
print('Tenha um dia abençoado {}'.format(nome))