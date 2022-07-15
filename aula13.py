
print('-=-'*2, 'START one', '-=-'*2)
for c in range(0, 6):
    print('Oi')

for c in range(0, 7, 2):
    print('Olá')

print('-=-'*2, 'FIM the one', '-=-\n'*2)

print('-=-'*2, 'START two', '-=-'*2)
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
    
print('-=-'*2, 'FIM the two', '-=-\n'*2)

print('-=-'*2, 'START three', '-=-'*2)
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    
print('-=-'*2, 'FIM the three', '-=-\n'*2)

print('-=-'*2, 'START four', '-=-'*2)

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    #s+=n
    s = s+n
print('O somatório de todos os valores foi {}'.format(s))
    
print('-=-'*2, 'FIM the four', '-=-\n'*2)
