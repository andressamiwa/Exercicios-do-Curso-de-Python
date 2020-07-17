'''
Aula 14
FOR
'''
'''
for n in range(1,11):
    print('Numero {}'.format(n))

for i in range(5):
    print('Curso')
    print('Python')

for n in range(10,0,-1):
    print('\n',n)

tabuada = 6
for num in range(1,11):
    print('{} x {} = {}'.format(num,tabuada,tabuada*num))

inicio = int(input('Inicio: '))
final = int(input('Final: '))
passo = int(input('Passo: '))

for i in range(inicio,final+1,passo):
    print('Numero {}'.format(i))

soma = 0
print('Digite numeros entre 0 e 10')
for num in range(0,3):
    n = int(input('Numero: '))
    if n<=10 and n >= 0:
        soma = soma +n
    else:
        print('Serao somados apenas numeros entre 0 e 10. {} nao sera somado'.format(n))

print('Soma = {}'.format(soma))

print('Inicio')

for num in range(0,6):
    print(num)
    if num == 2:
        break

print('Final')

for c in 'Curso de Python':
    print(c)
    if c == 'o':
        break

for c in 'Curso de Python':
    if c == 'o':
        continue
    print(c)

for c in 'Curso de Python':
    if c in 'ory':
        continue
    print(c)
'''
soma = 0
print('Digite numeros entre 0 e 10.\nA soma maxima sera 20')
for num in range(0,3):
    n = int(input('Numero: '))
    if n<=10 and n >= 0:
        soma = soma +n
    else:
        print('Serao somados apenas numeros entre 0 e 10. {} nao sera somado'.format(n))
    if soma >=20:
        soma = 20
        print('Valor maximo atingido')
        break
print('Soma = {}'.format(soma))
