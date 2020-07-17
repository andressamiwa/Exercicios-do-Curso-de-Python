'''

Curso de python
Aula 08: Formatação de strings, mensagens e números na tela

'''

cor = input('Escolha uma cor: ')
print('Cor escolhida {:10}.'.format(cor))
print('Cor escolhida {:>10}.'.format(cor))
print('Cor escolhida {:^10}.'.format(cor))
print('Cor escolhida {:<10}.'.format(cor))
print('Cor escolhida {:=^10}.'.format(cor))

n1 = 7
n2 = 3
#print('Soma {}.'.format(n1+n2))
s = n1+n2
m = n1-n2
d = n1/n2
di = n1//n2
e = n1**n2
print('Soma {} Multiplicação {} Divisão {:.2f} Divisão Inteira {} Potência {}'.format(s,m,d,di,e))

