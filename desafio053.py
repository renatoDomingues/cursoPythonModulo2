#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Ex: Apos a sopa; A sacada da casa; A torre da derrota; O lobo ama o bolo; Anotaram a data da maratona;

print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
print('Uma frase palíndromo são aquelas que dá para ler de frente e para a trás, sendo terão o mesmo significados, como exemplos uma frase palíndromo: "apos a sopa; A sacada da casa; A torre da derrota; O lobo ama o bolo; Anotaram a data da maratona".\n')

print('Digite uma frase qualquer abaixo: ')
frase = str(input('=> ').strip().upper())
print('Você digitou acima a frase: {}\n'.format(frase))

#frase2 = frase.replace(' ', '')
#fraseInv = frase2[::-1]
palavras = frase.split()
#print('Você digitou a frase {}'.format(palavras))
junto = ''.join(palavras)
#print('Você digitou a frase {}'.format(junto))
inverso = ''

#print(' => ', len(frase))
#print(' =>', len(frase.strip()))
'''
if frase2==fraseInv:
    print('A frase digitada acima é um PALÍNDROMO!!')
else:
    print('A frase acima NÃO é um PALÍNDROMO!!')
print('\n END!!')
'''
print('\nSTART\n')

for letra in range(len(junto)-1, -1, -1):
     #print(junto[letra])
     #inverso+=junto[letra]
     inverso = inverso+junto[letra]
if inverso==junto:
    print('Temos um PALÍNDROMO!!')
else:
    print('A frase digitada NÃO é um PALÍNDROMO!!')
print('A frase digitada acima {}'.format(junto), '<= =>', 'Modo inverso {}'.format(inverso))
print('\n END!!')

'''
* len => quando aplicada a um string, retorna o número de caracteres no string (ou seja, o seu comprimento);
* strip => retorna a string resultante a remoção do início e do final da string de todos caracterers em brancos; 
* lower => é um método embutido usado para manipulação de strings. Os métodos lower() retornam a string em minúsculas da string fornecida. Ele converte todos os caracteres maiúsculos em minúsculas. Se não houver caracteres maiúsculos, ele retornará a string original;
* replace => é usado para substituir trechos de uma string por uma ou mais vezes. Também podemos utilizar o módulo re, no qual podemos aplicar expressões regulares para refinar ainda mais as condições de substituição. Portanto, a linguagem oferece diversos recursos para a manipulação de strings.
Use as funções list() e join() para substituir um caractere em uma string.
Use a função bytearray() para substituir um caractere em uma string.
Use a função replace() para substituir caracteres em uma string.;
'''
    
print('\n', '-=-'*10, 'Tecnologia&Inovação DOMINGUES', '-=-'*10, '\n')
