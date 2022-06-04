def menor5(x):
    if x < 5:
        return True
    else:
        return False

def menor55(x):
    return x < 5

#menor5 = lambda x: x<5

lista = [0,1,2,3,4,5,6,7,9]
listar = filter(lambda x: x<5, lista)
lista2 = list(listar)

print(lista2)
