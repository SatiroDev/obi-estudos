n, m = input().split()
ingredientes = ['queijo', 'presunto', 'goiabada', 'azeitona']
N = int(n)
M = int(m)


verificacao = True
lista = []
subconjuntos = []
cont = 0
if 1 <= N and N <= 20 and 0 <= M and M <= 400:
    for i in range(M):
        x, y = input().split()
        X = int(x)
        Y = int(y)
        if 1 <= X and X <= N and 1<= X and X < Y:
            lista.append([X, Y])
            continue
        else:
            verificacao = False

    if verificacao:
        ind = 1
        while ind <= N:
            subconjuntos.append([ind])
            ind += 1
        for y in range(1, N+1):
            for z in  range(y, N+1):
                sub = [i for i in range(y, z+1) ]
                if sub not in subconjuntos:
                    subconjuntos.append(sub)
        for y in range(1, N+1):
            for z in  range(1, N+1):
                sub = [i for i in range(1, z+1, y) ]
                if sub not in subconjuntos:
                    subconjuntos.append(sub)
        
quantidade = 0

for ind in range(len(subconjuntos)):
    validacao = True
    for sub in lista:
        if sub[0] in subconjuntos[ind] and sub[1] in subconjuntos[ind]:
            validacao = False
            break
    if validacao:
        quantidade += 1
                


if verificacao:
    print(quantidade)




# Entrada
# 3 2
# 2 3
# 1 2

s = 0
# Por exemplo, suponha que num determinado dia N é igual a quatro e os ingrediantes são queijo, presunto, goiabada e azeitona, e M é igual a dois: os pares (goiabada, presunto) e (azeitona, goiabada) não podem ser utilizados no mesmo sanduíche. Nesse dia, alguns dos sanduíches que podem ser feitos são:

# presunto, queijo X
# azeitona 
# presunto, azeitona, queijo 
# goiabada, queijo 

# Alguns dos sanduíches que não podem ser feitos são:

# presunto, queijo, goiabada 
# azeitona, goiabada 
# goiabada, presunto, azeitona 