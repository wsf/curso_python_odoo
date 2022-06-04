from functools import reduce
lista = [1,2,3,4,5,6,7,9]
rl = reduce(lambda x,y: x*y, lista)
print(rl)

