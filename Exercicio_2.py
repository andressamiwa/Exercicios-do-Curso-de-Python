'''
Lista de Exercícios 2
'''

# Exercício 01
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1+n2
print('A soma de {} e {} vale {}'.format(n1, n2,soma))
# Exercício 02

dado = input('Digite qualquer informação: ')
print('Alfanumérico?',dado.isalnum())
print('Alfabético?',dado.isalpha())
print('ASCII?',dado.isascii())
print('Decimal?',dado.isdecimal())
print('Digito?',dado.isdigit())
print('Identificador?',dado.isidentifier())
print('Minúsculo?',dado.islower())
print('Numérico?',dado.isnumeric())
print('Printable?',dado.isprintable())
print('Espaço?',dado.isspace())
print('Título?',dado.istitle())
print('Maiúsculo',dado.isupper())

