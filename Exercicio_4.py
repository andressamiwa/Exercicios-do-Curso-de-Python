'''
Lista de Exercícios 4
'''

# Exercício 1

import math
import random
#n1 = float(input('Digite um numero real '))
#print('Numero {} - Parte inteira {}'.format(n1,math.floor(n1)))

# Exercício 2

#n2 = int(input('Angulo em graus '))
#n = (n2*3.1415)/180
#print('Numero {}'.format(n2))
#print('Seno {:.2f} - Cosseno {:.2f} - Tangente {:.2f}'.format(math.sin(n),math.cos(n),math.tan(n)))

# Exercício 3

n3 = input('Nome aluno 1 ')
n4 = input('Nome aluno 2 ')
n5 = input('Nome aluno 3 ')
vetor = [n3,n4,n5]
print('Aluno {}'.format(random.choice(vetor)))

