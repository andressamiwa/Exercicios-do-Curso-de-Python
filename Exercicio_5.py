'''
Lista de Exercícios 5
'''

# Exercício 1
nome=input('Qual o seu nome completo?')
print(nome.upper())
print(nome.lower())
palavras=nome.split()
print(''.join(palavras))
nome1=''.join(nome.split())
print(len(nome1))
print(len(palavras[0]))

# Exercício 2
num = input('Digite um numero entre 0 e 999')
num1 = int(num)
if num1>999:
    print('Invalido')
elif num1<0:
    print('Invalido')
else:
    print('Numero:' + num)
if num1>99:
    print('Unidade:'+ num[2])
    print('Dezena:'+ num[1])
    print('Centena:'+ num[0])
elif 9<num1<99:
    print('Dezena:' + num[1])
    print('Unidade:' + num[0])
else:
    print('Unidade:' + num[0])

# Exercício 3
cidade = input('Qual o nome da sua cidade?')
cidade=cidade.upper()
print('SAO' in cidade)


# Exercício 4
nome1 = input('Qual o seu nome?')
nome1=nome1.upper()
print('SILVA' in nome1)

# Exercício 5
frase = input('Digite uma frase')
frase = frase.lower()
print(frase.count('a'))
print(frase.find('a')
print(frase.rfind('a'))