'''

Curso de python
Aula 09: Utilizacao de modulos, bibliotecas e funcoes

'''

import math
import emoji
num = int(input('Digite um numero '))
raiz = math.sqrt(num)
print('Numero {} - Raiz {:.2f}'.format(num,raiz))
print('Numero {} - Raiz {:.2f}'.format(num,math.ceil(raiz)))
print('Numero {} - Raiz {:.2f}'.format(num,math.floor(raiz)))
print('Numero {} - Pot. {:.2f}'.format(num,math.pow(2,3)))
print(emoji.emojize('Tudo bem :smile:', use_aliases=True))
