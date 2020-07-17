'''
Aula 11 - Condicionais no python
'''

#exemplo com if, else
#idade = int(input('Qual a sua idade? '))
#if idade < 18:
#    print('Apenas maiores de 18 podem entrar.')

#else:
#    print('Ola! Aproveite o nosso bar!')
#    bebida = str(input('Qual bebida voce deseja? '))
#    print('Aqui esta sua bebida: {}'.format(bebida))

#exemplo com elif
#idade = int(input('Qual a sua idade? '))
#if idade <18:
#    print('Apenas maiores de 18 podem entrar')
#elif idade >=18 and idade <21:
#    print('Voce pode consumir refrigerantes!')
#else:
#    print('Bem vindo!')
#    bebida = str(input('Qual bebida deseja? '))
#    print('Aqui está sua bebida {}'.format(bebida))

#exemplo com or
numero = str(input('Escolha um numero de 1 a 4 '))
if numero == '1' or numero == '3':
    print('O numero é impar')
else:
    print('O numero é par')