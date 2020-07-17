'''

Aula 17
Listas e Tuplas

'''
'''
lista1 = [1,2,3] #primeira forma de declarar listas
lista2 = list(('a',True,2)) #segunda forma de declarar listas
lista = [['Ana','Matheus','Julio'],[15,37,52,64]]
print(lista)
nomes = lista[0]
idades = lista[1]
print(nomes)
print(idades)
print(idades[1])
print(lista[0][2])
print(lista[1][2])
print('{} possui {} anos.'.format(lista[0][0],lista[1][0]))
print('{} possui {} anos.'.format(lista[0][1],lista[1][1]))
print('{} possui {} anos.'.format(lista[0][2],lista[1][2]))

lista = [1,2,3,4,5,6]

i =0
qtd = len(lista)
while i < qtd:
    print(lista[i])
    i +=1

for i in lista:
    print(i)

for id in range(len(lista)):
    lista[id] += 50
print(lista)
'''
lista = [1,2,3,4,5,6]
for id, item in enumerate(lista):
    lista[id] +=1000
print(lista)