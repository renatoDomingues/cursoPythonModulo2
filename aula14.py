
print('\nMetodo de repetição FOR\n')

for c1 in range(1, 10):
    print(c1)
print('END')

c2 =1
print('\nMetodo de repetição WHILE\n')

while c2<10:
    print(c2)
    c2=c2+1
print('END')

print('\nExercicio com FOR\n')

for c3 in range(1, 5):
    v = int(input('Digite um valor: '))
print('Obrigado\n')

print('\nExercicios com WHILE\n')

n =1
while n!=0:
    n = int(input('Digite um valor: '))
print('Obrigado\n')

r ='S'
while r=='S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('END\n')

n =1
par =impar=0
while n!=0:
    n =int(input('Digite um valor: '))
    if n!=0:
        if n%2==0:
            #par+=1
            par = par+1
        else:
            #impar+=1
            impar = impar+1
print('Você digitou {} números pares e {} números impares'.format(par, impar))
