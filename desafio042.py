#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: -Equilátero: todos os lados são iguais; -Isósceles: dois lados iguais; -Escaleno: todos os lados diferentes;

print('-=' *10, 'ANALISADOR DE TRIÂNGULOS', '-=-' *10)
print('Esse sofware calcula se pode ou não, de formar um triângulo e junto qual será, se é um triângulo Equilátero, Isósceles ou Escaleno!')
print('Triângulo EQUILÁTERO: todos os lados iguais; \nTriângulo ISÓSCELES: dois lados iguais; \nTriângulo ESCALENO: todos os lados diferentes;')
print(' ')
rta1 = float(input('Digite um número: '))
rta2 = float(input('Digite o segundo número: '))
rta3 = float(input('Agora, digite o terceiro número: '))
print('Você digitou acima os números {}, {} e {}'.format(rta1, rta2, rta3))
print(' ')

#if rta1<rta2+rta3 and rta2<rta1+rta3 and rta3<rta1+rta2:
#if rta1==rta2 and rta2==rta3:
#if rta1==rta2==rta3:
#if (rta1*rta2==rta2*rta3==rta1*rta3)==True:
#elif (rta1*rta2==rta1*rta3)==True:
#elif (rta1*rta2!=rta2*rta3!=rta1*rta3)==True:

if (rta2-rta3)<rta1<(rta2+rta3) and (rta1-rta3)<rta2<(rta1+rta3) and (rta1-rta2)<rta3<(rta1+rta2):
    if rta1==rta2==rta3:
        print('É possível formar um triângulo, pois o mesmo será um triângulo Equilátero!')
    elif rta1==rta2 or rta2==rta3 or rta3==rta1:
        print('É possível formar um triângulo, pois o mesmo será um triângulo Isosceles!')
    elif rta1!=rta2!=rta3!=rta1:
        print('É possível formar um triângulo, pois o mesmo será um triângulo Escaleno!')
else:
    print('ERRO, desculpe não foi possivel formar um triângulo, pois por favor tente novamente ...')
    
print(' ')
print('-=-' *15, 'FIM', '-=-' *15)
