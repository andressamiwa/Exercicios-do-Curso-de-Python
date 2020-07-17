'''
Lista de Exercicios
'''

#Exercicio 1
#valor = int(input('Valor do Imóvel R$ ?'))
#salario = int(input('Valor do seu salario R$ ?'))
#tempo = int(input('Em quantos anos erá realizado o pagamento? ?'))
#prestacao = valor / (tempo * 12)
#if prestacao < 0.3*salario:
#    print('Parabens! Empréstimo aprovado de R$ {}'.format(prestacao))
#else:
#    print('Desculpe, mas nao podemos aprovar o seu emprestimo. \nO valor de R$ {:.2f} e maior do que podemos aprovar de acordo com seu salario, que e de R$ {:.2f}'.format(prestacao,salario*0.3))

#Exercicio 2
#Numeroum = int(input('Numero 1: '))
#Numerodois = int(input('Numero 2: '))
#if Numeroum>Numerodois:
#    print('O primeiro numero é maior que o segundo.')
#elif Numerodois>Numeroum:
#    print('O segundo numero é maior que o primeiro.')
#else:
#    print('Os dois valores sao iguais.')

#Exercicio 3
#ano = int(input('Qual o seu ano de nascimento? '))
#if (2020 - ano) == 18:
#    print('Esse é o seu ano de alistamento')
#elif (2020 - ano) < 18:
#    print('Voce irá se alistar dentro de {} anos'.format(18-(2020-ano)))
#else:
#    print('Já passou seu ano de alistamento')

#Exercicio 4
#notaum = int(input('Nota 1: '))
#notadois = int(input('Nota 2: '))
#media = (notaum + notadois)/2
#if media <5:
#    print('Aluno \033[1;31mReprovado\033[m! Media {}'.format(media))
#elif media >= 5 and media < 6.9:
#    print('Aluno de \033[1;32mRecuperacao\033[m! Media {}'.format(media))
#else:
#    print('Aluno \033[1;33mAprovado\033[m! Media {}'.format(media))

#Exercicio 5
peso = int(input('Seu peso: '))
altura = float(input('Sua altura: '))
imc = peso/(altura**2)
if imc < 18.5:
    print('Seu IMC = {}. \nAbaixo do peso!'.format(imc))
elif imc >= 18.5 and imc <25:
    print('Seu IMC = {}. \nPeso ideal!'.format(imc))
elif imc >= 25 and imc <30:
    print('Seu IMC = {}. \nSobrepeso!'.format(imc))
elif imc >= 30 and imc <40:
    print('Seu IMC = {}. \nObesidade!'.format(imc))
else:
    print('Seu IMC = {}. \nObesidade Morbida!'.format(imc))

#Exercicio 6
valor = float(input('Qual o valor do livro: R$ '))
print('Forma de pagamentos: \n1 - A vista com dinheiro \n2 - A vista com cartao \n3 - Em 2x no cartao \n4 - 3 ou mais vezes no cartao')
forma = int(input('Qual a sua forma de pagamento?'))
if forma == 1:
    print('O valor a ser pago é R$ {:.2f}'.format(valor*0.9))
elif forma == 2:
    print('O valor a ser pago é R$ {:.2f}'.format(valor * 0.95))
elif forma == 3:
    print('O valor a ser pago é R$ {:.2f}'.format(valor))
else:
    print('O valor a ser pago é R$ {:.2f}'.format(valor * 1.2))