'''
Lista de Exercícios 6
'''

#exercicio 1
import random
sorteado = int(input('Qual o numero sorteado de 0 a 5 '))
computador = random.randint(0,5)
if sorteado == computador:
    print('Voce \033[1;32macertou\033[m! O numero sorteado é o {}'.format(computador))
else:
    print('Voce \033[1;31merrou\033[m o numero sorteado foi {}'.format(computador))

#exercicio 2
velocidade = int(input('Qual a velocidade do seu carro em km/h? '))
if velocidade > 80:
    multa = (velocidade-80)*5
    print('Voce foi \033[1;31mmultado\033[m em {} reais'.format(multa))

#exercicio 3
numero = int(input('Digite um numero inteiro '))
if numero%2==0:
    print('Este numero e par')
else:
    print('Esse numero é impar')

#exercicio 4
distancia = int(input('Qual a distancia da viagem em km? '))
if distancia <=100:
    print('O valor da \033[1;34mpassagem\033[m e R$ {}.'.format(distancia*0.6))
else:
    print('O valor da \033[1;34mpassagem\033[m e R$ {}'.format(distancia*0.5))

#exercicio 5
ano = int(input('Qual o ano? '))

if ano%4 ==0 and ano%100!=0:
    print('Ano bissexto!')
elif ano%100 and ano%400 == 0:
        print('O ano é bissexto!')
else:
    print('O ano não é bissexto')

#exercicio 6
salario = int(input('Qual o seu \033[1;33msalario\033[m atual em R$?'))
if salario<=1500:
    print('Novo \033[1;33msalario\033[m: R${}'.format(salario*1.2))
else:
    print('Novo salario: R${}'.format(salario*1.1))