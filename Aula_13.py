'''
Aula 13
Condicoes aninhadas
'''

nome = input('Qual o seu nome?')
if nome == 'Andressa':
    print('Que nome bonito!')
elif nome == 'Bruna' or nome == 'Regina':
    print('Nome de princesa!')
elif nome in 'Natalia Julia Amanda':
    print('Nome muito interessante')
else:
    print('Seu nome é normal')
print('Vá com cuidado {}!'.format(nome))

idade = int(input('Qual a sua idade?'))
if idade < 18:
    print('Apenas pessoas com 18 anos ou mais podem entrar!')
else:
    print('Bem-Vindo ao bar!')
    if idade<=21:
        print('Voce pode pedir refrigerante!')
    elif 21 < idade and idade <= 60:
        print('Voce pode pedir cerveja e vodka!')
    else:
        print('Voce pode pedir agua!')