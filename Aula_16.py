'''

Aula 16
Listas e tuplas

'''
'''
numeros = [8,9,10,11,12]
print(numeros)
print(numeros[1])
print(numeros[2])
print(numeros[0])
print(numeros[-1])
string = ['a','b','c','d','Python']
print(string)
print(string[0])
print(string[-1])
lista = list(('Python'))
print(lista)
lista_mista = [1,4,5,'c',True,'Curso de Python',0]
print(lista_mista)
print(lista_mista[6])

for i in lista_mista:
    print(i)


lista1 = ['a', 'b','c']
lista2 = ['d', 'e','f']
lista = lista1+lista2
print(lista)

lista1 = ['a','b','c']
lista2 = [1,3,7]
lista3 = [True, False]
lista4 = ['Ana','Julia','Rafael']
lista = lista1+lista2+lista3+lista4
print(lista)


numeros = [1,2,3]
print(numeros)
numeros.append(7)
print(numeros)

lista = []
lista.append(1)
lista.append(2)
lista.append(3)
print(lista)

nomes = []
while True:
    nome = input('Digite um nome: ')
    if len(nome) ==0:
        break
    else:
        nomes.append(nome)
print(nomes)
'''

num =[1,3,4,5,6,7]
print(num)
del(num[1])
print(num)