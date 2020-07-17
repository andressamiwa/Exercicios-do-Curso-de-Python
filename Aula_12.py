'''
Aula 12
'''

#como mudar a cor, da fonte e do fundo, utilizando o padrao ANSI

print('\033[0;32;41mTeste de cor\033[m')
print('\033[2;35;43mTeste de cor\033[m')
print('\033[1;31;45mTeste de cor\033[m')

n = 10
print('O numero é: \033[1;31m{}\033[m'.format(n))
print('O numero é: {}{}{}'.format('\033[31m',n,'\033[m'))
