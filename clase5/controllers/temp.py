f = lambda x:x+100
r = f(1)
print(r)

filtro = lambda x: True if (x>5) else False

lista = [1,2,3,4,5,6,7]

rl = map(f, lista)
rl = filter(filtro,lista)

print(*rl)

from functools import reduce

def f2(x,y):
    return x+y

rl = reduce(f2, lista)
print(rl)
