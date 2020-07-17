'''

Curso de python
Aula 07 : Atribuição Múltipla, Operadores compostos, Atribuição condicional

'''

#atribuicao multipla

x,y,z,w = 10, 20, 30, 50
print('{} {} {} {}'.format(x,y,z,w))

#operadores compostos
mais = menos = vezes = dividido = 2

#mais = mais + 2
mais +=2
print(mais)

menos -= 5
print(menos)

vezes *=5
print(vezes)

dividido =9
dividido /= 3
print(dividido)

#Atribuicao condicional
nota = 6

if nota >= 7:
    situacao = 'Aprovado!'
else:
    situacao = 'Reprovado!'

print('O aluno com nota {} está {}'.format(nota,situacao))

#situacao = 'Aprovado' if nota >= 7 else 'Reprovado'

