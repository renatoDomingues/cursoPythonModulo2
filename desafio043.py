#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: -Abaixo de 18.5; abaixo de peso; -Entre 18.5 e 25: peso ideal; -De 25 at´30: Sobrepeso; =De 30 até 40: Obesidade; -Acima de 40: Obesidade mórbida;

print(' !!Startup Tecnologia&Inovação Domingues!!' *2)
print(' ')
print('Esse programa foi desenvolvido para calcular o seu IMC "Indice Massa Corporal" para mostrar de acordo com uma tabela, se a pessoa está ou não acima do seu peso')
print('Abaixo de 18.5: peso está abaixo\n De 18.5 até 25: peso está ideal\n De 25 até 30: peso em sobrepeso\n De 30 até 40: peso em obesidade\n Acima de 40: peso em obesidade mórbida')
print(' ')

print('Digite o seu peso abaixo: ')
pso = float(input('=> '))
print('Digite a sua altura abaixo: ')
atura = float(input('=> '))
print('O seu peso {}Kg e a sua altura {}m foi digitada acima.'.format(pso, atura))
print(' ')

#9**2
#9**(1/2)
#9**0.5
#imc = pso/(atura*atura)
imc = pso/(atura**2)

print('O IMC do peso com altura digitado acima foi {:.1f}'.format(imc))
print('AGUARDE um momento, calculando ...')
print(' ')

if imc<18.5:
    print('Você está ABAIXO do peso!!')
elif imc>=18.5 and imc<25:
    print('PARABÉNS, tu está com peso IDEAL!!')
elif imc>=25 and imc<30:
    print('SINAL AMARELO, seu peso está em SOBREPESO!!')
    print('Procure se alimentar melhor e junto realizar exercicios diarios.')
elif imc>=30 and imc<40:
    print('ATENÇÃO, seu peso está acima, em OBESIDADE!!')
    print('Alem de se alimentar melhor e realizar exercicios, procure um medico.')
elif imc>40:
    print('CUIDADO, o seu peso está muito acima, em OBESIDADE MÓRBIDA')
    print('Procure um médico.')
    
print(' ')
print('Obrigado pela a confiança em nossos trabalhos.')
