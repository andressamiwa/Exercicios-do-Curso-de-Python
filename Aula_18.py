'''

Aula 18

'''
'''
lista = ['a','b','c','d','e','f']
print(lista)
print(lista[2:5])
num = [0,1,2,3,4,5,6,7,8,9,10]
pares = num[::2]
print(pares)
impares = num[1:6:2]
print(impares)
'''
#inclusao
'''
num = [1,2,3,4,5]
print(num)
num.append(10)
print(num)
num.insert(0,20)
print(num)

num.insert(3,50)
print(num)
num.insert(-1,80)
print(num)

#alterando
num = [1,2,3,4,5]
num[1]='D'
num[2]='p'
print(num)

#deletando
del(num[1])
print(num)

del(num[2:4])
print(num)

num.clear()
print(num)
'''
num = [1,2,3,4,5]
print(num)
print(num.pop())
print(num)